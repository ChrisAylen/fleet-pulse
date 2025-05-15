import requests
import random
import time

# Central London
CENTER_LAT = 51.5074
CENTER_LON = -0.1278

# Simulate 10 vehicles
NUM_VEHICLES = 10
VEHICLES = [f"veh-{i:03d}" for i in range(NUM_VEHICLES)]

def random_offset():
    return random.uniform(-0.01, 0.01)

def simulate_ping(vehicle_id):
    lat = CENTER_LAT + random_offset()
    lon = CENTER_LON + random_offset()
    vtype = random.choice(["van", "bike", "car"])

    payload = {
        "vehicle_id": vehicle_id,
        "lat": lat,
        "lon": lon,
        "type": vtype
    }

    try:
        res = requests.post("http://127.0.0.1:8000/ping", json=payload)
        if res.status_code == 200:
            print(f"✅ Sent ping: {vehicle_id} ({lat:.4f}, {lon:.4f})")
        else:
            print(f"❌ Error: {res.status_code}")
    except Exception as e:
        print(f"⚠️  Failed to send ping: {e}")

if __name__ == "__main__":
    while True:
        for vehicle_id in VEHICLES:
            simulate_ping(vehicle_id)
        time.sleep(2)  # Every 2 seconds, send all vehicle pings
