# Fleet Pulse

Fleet Pulse is a lightweight, real-time fleet visualisation demo that uses **Uber H3** spatial indexing, **Leaflet.js**, and **FastAPI** to simulate and display vehicle movement in central London.

This project showcases:

* Real-time hex-based heatmapping of vehicle density (H3)
* Full GPS trails per vehicle
* Vehicle type filtering and map controls
* Clean, modular architecture (Python + HTML/JS)

---

## ✨ Features

* 📉 **Live Heatmap:** Real-time hexagonal heatmap using Uber's H3 geospatial indexing
* 🚗 **Simulated Fleet:** 10 randomised vehicles sending GPS pings every 2 seconds
* 🛀 **Vehicle Trails:** Shows last-known GPS path for each vehicle
* 🌐 **Web Map:** Fast, interactive map built with Leaflet
* ⚖️ **Filter Controls:** Toggle trails, markers, and filter by vehicle type

---

## 📁 Project Structure

```
fleet_pulse/
├── main.py               # FastAPI backend and routing
├── simulator.py          # Simulated vehicle GPS pings
├── templates/
│   └── map.html        # HTML + Leaflet.js frontend
├── static/               # (optional CSS/images)
├── requirements.txt
```

---

## ⚡ Getting Started

### 1. Clone & Install

```bash
git clone https://github.com/your-username/fleet-pulse.git
cd fleet-pulse
pip install -r requirements.txt
```

### 2. Run the Backend

```bash
uvicorn main:app --reload
```

### 3. Start the Simulator

In a second terminal:

```bash
python simulator.py
```

### 4. Open Your Browser

Go to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

You should see:

* H3 hex heatmap building up
* Trails and last positions for vehicles
* Filters in top-left corner

---

## 🌍 Tech Stack

* **Backend:** Python, FastAPI, Jinja2
* **Frontend:** HTML5, Leaflet.js, H3.js (client-side H3 rendering)
* **Simulated Data:** Python script with randomised walk

---

## ⚖️ Controls

* ☑️ **Show Trails:** Toggle GPS trails for vehicles
* ☑️ **Show Markers:** Display last known location of each vehicle
* ▼ **Filter Type:** Only show vehicles of selected type (van, car, bike)

---

## 🔄 Real-Time Logic

* Vehicles send pings every 2 seconds to `/ping`
* Backend bins GPS into H3 cells (resolution 9) and stores short trails
* `/heatmap` and `/trails` endpoints return live data
* Frontend fetches and re-renders every 3 seconds

---

## 🔍 Customisation Ideas

* Add real vehicle icons (SVG by type)
* Show tooltips on marker hover (vehicle ID, timestamp)
* Animate past playback (sliding time window)
* Save data for replay/debug sessions

---

## 🚫 Limitations

* Not connected to real GPS or external sources
* No database; in-memory only
* For demo/educational purposes, not production-ready

---

## 📄 License

MIT. Feel free to use and adapt.

---

## 👋 Credits

* Inspired by Uber's [H3 spatial indexing](https://h3geo.org)
* Mapping with [Leaflet.js](https://leafletjs.com)
* Backend powered by [FastAPI](https://fastapi.tiangolo.com)

---

Enjoy your live fleet visualisation! 🚗📊
