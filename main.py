# main.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import h3
import uvicorn
from collections import defaultdict, deque
import time

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# In-memory storage of counts per H3 hex
# Store per-hex pings as a deque of timestamps
hex_pings = defaultdict(deque)
PING_LIFESPAN = 60  # seconds
resolution = 9
resolution = 9

MAX_TRAIL_LENGTH = 5
vehicle_trails = defaultdict(lambda: deque(maxlen=MAX_TRAIL_LENGTH))
vehicle_types = {}  # vehicle_id -> type


class Ping(BaseModel):
    vehicle_id: str
    lat: float
    lon: float
    type: str = "van"

@app.post("/ping")
async def receive_ping(ping: Ping):
    h3_index = h3.geo_to_h3(ping.lat, ping.lon, resolution)
    now = time.time()

    # Save to time-decayed hexmap
    hex_pings[h3_index].append(now)

    # Save full GPS point trail
    vehicle_trails[ping.vehicle_id].append((ping.lat, ping.lon, time.time()))
    vehicle_types[ping.vehicle_id] = ping.type

    return {"status": "ok", "h3": h3_index}

@app.get("/heatmap")
def get_heatmap():
    now = time.time()
    response = []

    for h3_index, timestamps in hex_pings.items():
        # Remove expired pings
        while timestamps and now - timestamps[0] > PING_LIFESPAN:
            timestamps.popleft()

        if timestamps:  # Still has active pings
            response.append({
                "h3": h3_index,
                "count": len(timestamps)
            })

    return JSONResponse({ "hexes": response })

@app.get("/trails")
def get_trails():
    trails = []
    for vehicle_id, coords in vehicle_trails.items():
        print(f"[TRAIL DEBUG] {vehicle_id}: {list(coords)}")
        if coords:
            trails.append({
                "vehicle_id": vehicle_id,
                "type": vehicle_types.get(vehicle_id, "unknown"),
                "path": [{"lat": lat, "lon": lon} for lat, lon, _ in coords]
            })
    return JSONResponse({ "trails": trails })

@app.get("/", response_class=HTMLResponse)
async def show_map(request: Request):
    return templates.TemplateResponse("map.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
