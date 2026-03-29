"""Main pipeline: update route archive, then build historical outputs."""

import json
import os

from flights import Flight, FlightMap, FlightRoute
from flights.History import append_row as append_history
from flights.Post import Post
from flights.ReadMe import ReadMe


def main():
    # Fetch recently completed routes so the archive keeps growing.
    routes = FlightRoute.fetch_routes(hours=2)

    if routes:
        FlightRoute.save_routes(routes)

    # Rebuild the outputs from every saved historical route file.
    saved_routes = FlightRoute.load_saved_routes()
    summary = Flight.compute_historical_summary(saved_routes)

    os.makedirs("data", exist_ok=True)
    with open(os.path.join("data", "summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print(
        "Summary saved: "
        f"{summary['total_flights']} archived flights, "
        f"{summary['unique_routes']} unique routes"
    )

    FlightMap([], summary).create_map()
    ReadMe(summary).write()
    Post(summary).write()
    append_history(summary)


if __name__ == "__main__":
    main()
