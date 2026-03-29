"""Generate DAILY_REPORT.md by aggregating data/history.csv snapshots."""

import csv
import os
from datetime import datetime, timezone

from flights.ReadMe import _flag

HISTORY_PATH = os.path.join("data", "history.csv")
REPORT_PATH = "DAILY_REPORT.md"


def _read_history() -> list[dict]:
    """Read all rows from the history CSV."""
    if not os.path.isfile(HISTORY_PATH):
        return []
    with open(HISTORY_PATH, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _int(val: str, default: int = 0) -> int:
    try:
        return int(float(val))
    except (ValueError, TypeError):
        return default


def _float(val: str, default: float = 0.0) -> float:
    try:
        return float(val)
    except (ValueError, TypeError):
        return default


def generate() -> None:
    """Generate the daily report from history data."""
    rows = _read_history()
    if not rows:
        print("No history data found, skipping daily report.")
        return

    now = datetime.now(timezone.utc)
    now_str = now.strftime("%Y-%m-%d %H:%M UTC")

    # Parse all rows with their timestamps
    entries = []
    for r in rows:
        entries.append({
            "datetime_utc": r.get("datetime_utc", ""),
            "total_flights": _int(r.get("total_flights")),
            "unique_routes": _int(r.get("unique_routes")),
            "countries": _int(r.get("countries")),
            "airports": _int(r.get("airports")),
            "airlines": _int(r.get("airlines")),
            "avg_duration_min": _int(r.get("avg_duration_min")),
            "total_distance_km": _float(r.get("total_distance_km")),
            "total_co2_tonnes": _float(r.get("total_co2_tonnes")),
            "avg_distance_km": _float(r.get("avg_distance_km")),
        })

    # Group by date
    by_date: dict[str, list[dict]] = {}
    for e in entries:
        date = e["datetime_utc"][:10]
        by_date.setdefault(date, []).append(e)

    dates = sorted(by_date.keys())

    # Latest entry
    latest = entries[-1]

    # Build report
    lines = [
        "# Daily Air Traffic Report",
        "",
        f"*Generated {now_str}*",
        "",
        "---",
        "",
        "## Current Totals",
        "",
        f"- **{latest['total_flights']:,}** total flights archived",
        f"- **{latest['unique_routes']:,}** unique routes",
        f"- **{latest['countries']}** countries",
        f"- **{latest['airports']}** airports",
        f"- **{latest['airlines']}** airlines",
        f"- **{latest['total_co2_tonnes']:,.1f} tonnes** estimated CO2",
        f"- **{latest['total_distance_km']:,.0f} km** total distance flown",
        "",
        "## Daily Growth",
        "",
        "| Date | Flights | Routes | Countries | Airports | CO2 (t) |",
        "|------|--------:|-------:|----------:|---------:|--------:|",
    ]

    for date in dates[-30:]:  # Last 30 days
        day_entries = by_date[date]
        last = day_entries[-1]
        lines.append(
            f"| {date} | {last['total_flights']:,} | "
            f"{last['unique_routes']:,} | {last['countries']} | "
            f"{last['airports']} | {last['total_co2_tonnes']:,.1f} |"
        )

    # Day-over-day changes (last 7 days)
    if len(dates) >= 2:
        lines += [
            "",
            "## Day-over-Day Changes (last 7 days)",
            "",
            "| Date | New Flights | New Routes | CO2 Change (t) |",
            "|------|------------:|-----------:|---------------:|",
        ]
        recent_dates = dates[-8:]  # Need N+1 to compute N diffs
        for i in range(1, len(recent_dates)):
            prev_day = by_date[recent_dates[i - 1]][-1]
            curr_day = by_date[recent_dates[i]][-1]
            new_flights = curr_day["total_flights"] - prev_day["total_flights"]
            new_routes = curr_day["unique_routes"] - prev_day["unique_routes"]
            co2_change = curr_day["total_co2_tonnes"] - prev_day["total_co2_tonnes"]
            sign = "+" if co2_change >= 0 else ""
            lines.append(
                f"| {recent_dates[i]} | +{new_flights:,} | "
                f"+{new_routes:,} | {sign}{co2_change:,.1f} |"
            )

    lines += [
        "",
        "---",
        "",
        f"*Data from {len(entries)} pipeline snapshots across {len(dates)} days*",
        "",
    ]

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Daily report written to {REPORT_PATH}")
