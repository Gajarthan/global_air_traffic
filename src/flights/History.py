"""Append a row to data/history.csv each pipeline run for trend tracking."""

import csv
import os
from datetime import datetime, timezone


HISTORY_PATH = os.path.join("data", "history.csv")

COLUMNS = [
    "timestamp",
    "datetime_utc",
    "total_flights",
    "unique_routes",
    "countries",
    "airports",
    "airlines",
    "avg_duration_min",
    "total_distance_km",
    "total_co2_tonnes",
    "avg_distance_km",
]


def append_row(summary: dict) -> None:
    """Append one row of stats from a summary dict to the history CSV."""
    os.makedirs(os.path.dirname(HISTORY_PATH), exist_ok=True)

    file_exists = os.path.isfile(HISTORY_PATH)

    ts = summary.get("timestamp", 0)
    dt = datetime.fromtimestamp(ts, timezone.utc)

    row = {
        "timestamp": ts,
        "datetime_utc": dt.strftime("%Y-%m-%d %H:%M:%S"),
        "total_flights": summary.get("total_flights", 0),
        "unique_routes": summary.get("unique_routes", 0),
        "countries": len(summary.get("countries", {})),
        "airports": len(summary.get("top_airports", [])),
        "airlines": len(summary.get("airlines", {})),
        "avg_duration_min": summary.get("avg_duration_min", 0),
        "total_distance_km": summary.get("total_distance_km", 0),
        "total_co2_tonnes": summary.get("total_co2_tonnes", 0),
        "avg_distance_km": summary.get("avg_distance_km", 0),
    }

    with open(HISTORY_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)

    print(f"History row appended to {HISTORY_PATH}")
