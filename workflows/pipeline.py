"""Main pipeline: fetch global flights, generate map and stats."""

import json
import os

from flights import Flight, FlightMap, FlightRoute
from flights.Post import Post
from flights.ReadMe import ReadMe


def main():
    # 1. Fetch live aircraft positions from OpenSky Network
    flights = Flight.fetch_live()

    # 2. Fetch completed flight routes (from→to, last 2 hours)
    routes = FlightRoute.fetch_routes(hours=2)

    # 3. Save individual route files to data/flights/
    if routes:
        FlightRoute.save_routes(routes)

    # 4. Compute summary statistics
    summary = Flight.compute_summary(flights, routes)

    # 5. Save summary to data/summary.json
    os.makedirs("data", exist_ok=True)
    with open(os.path.join("data", "summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    print(f"Summary saved: {summary['total_aircraft']} aircraft, {summary['route_count']} routes")

    # 6. Generate outputs
    FlightMap(flights, summary).create_map()
    ReadMe(summary).write()
    Post(summary).write()


if __name__ == "__main__":
    main()
