"""Generate LEADERBOARD.md with weekly top-10 rankings."""

import json
import os
from datetime import datetime, timezone
from collections import Counter

from flights.Flight import FlightRoute, _callsign_airline
from flights.ReadMe import _flag


LEADERBOARD_PATH = "LEADERBOARD.md"


def generate() -> None:
    """Generate weekly leaderboard from all archived route files."""
    routes = FlightRoute.load_saved_routes()
    if not routes:
        print("No routes found, skipping leaderboard.")
        return

    now = datetime.now(timezone.utc)
    now_str = now.strftime("%Y-%m-%d %H:%M UTC")

    # --- Compute rankings ---

    # Top airlines by flight count
    airline_counts: Counter = Counter()
    for r in routes:
        airline = r.airline or _callsign_airline(r.callsign)
        if airline:
            airline_counts[airline] += 1

    # Top airports (departures + arrivals)
    airport_counts: Counter = Counter()
    airport_names: dict[str, str] = {}
    airport_countries: dict[str, str] = {}
    for r in routes:
        for icao, name, country in (
            (r.dep_airport_icao, r.dep_airport_name, r.dep_country),
            (r.arr_airport_icao, r.arr_airport_name, r.arr_country),
        ):
            if icao:
                airport_counts[icao] += 1
                airport_names.setdefault(icao, name or icao)
                airport_countries.setdefault(icao, country or "")

    # Top routes by frequency
    route_pairs: Counter = Counter()
    route_info: dict[str, dict] = {}
    for r in routes:
        key = f"{r.dep_airport_icao}-{r.arr_airport_icao}"
        route_pairs[key] += 1
        route_info.setdefault(key, {
            "dep": f"{r.dep_airport_name} ({r.dep_airport_icao})",
            "arr": f"{r.arr_airport_name} ({r.arr_airport_icao})",
            "distance_km": round(r.distance_km, 1),
        })

    # Top countries
    country_counts: Counter = Counter()
    for r in routes:
        for c in (r.dep_country, r.arr_country):
            if c:
                country_counts[c] += 1

    # Longest flights by distance
    longest = sorted(
        (r for r in routes if r.distance_km > 0),
        key=lambda r: r.distance_km,
        reverse=True,
    )[:10]

    # Highest CO2 single flights
    highest_co2 = sorted(
        (r for r in routes if r.co2_kg > 0),
        key=lambda r: r.co2_kg,
        reverse=True,
    )[:10]

    # --- Build markdown ---
    lines = [
        "# Weekly Air Traffic Leaderboard",
        "",
        f"*Generated {now_str} | {len(routes):,} flights archived*",
        "",
        "---",
        "",
        "## Top 10 Airlines",
        "",
        "| # | Airline | Flights |",
        "|---:|---------|--------:|",
    ]
    for idx, (airline, count) in enumerate(airline_counts.most_common(10), 1):
        lines.append(f"| {idx} | {airline} | {count:,} |")

    lines += [
        "",
        "## Top 10 Airports",
        "",
        "| # | Airport | Country | Flights |",
        "|---:|---------|---------|--------:|",
    ]
    for idx, (icao, count) in enumerate(airport_counts.most_common(10), 1):
        name = airport_names.get(icao, icao)
        country = airport_countries.get(icao, "")
        flag = _flag(country)
        lines.append(f"| {idx} | {name} ({icao}) | {flag} {country} | {count:,} |")

    lines += [
        "",
        "## Top 10 Routes",
        "",
        "| # | From | To | Flights | Distance |",
        "|---:|------|-----|--------:|---------:|",
    ]
    for idx, (key, count) in enumerate(route_pairs.most_common(10), 1):
        info = route_info[key]
        dist = f"{info['distance_km']:,.0f} km" if info['distance_km'] else "-"
        lines.append(f"| {idx} | {info['dep']} | {info['arr']} | {count:,} | {dist} |")

    lines += [
        "",
        "## Top 10 Countries",
        "",
        "| # | Country | Flights |",
        "|---:|---------|--------:|",
    ]
    for idx, (country, count) in enumerate(country_counts.most_common(10), 1):
        lines.append(f"| {idx} | {_flag(country)} {country} | {count:,} |")

    lines += [
        "",
        "## Longest Flights (by distance)",
        "",
        "| # | Callsign | From | To | Distance | Duration | CO2 |",
        "|---:|----------|------|-----|--------:|---------:|----:|",
    ]
    for idx, r in enumerate(longest, 1):
        dep = f"{r.dep_airport_name} ({r.dep_airport_icao})"
        arr = f"{r.arr_airport_name} ({r.arr_airport_icao})"
        lines.append(
            f"| {idx} | {r.callsign} | {dep} | {arr} | "
            f"{r.distance_km:,.0f} km | {r.duration_str} | "
            f"{r.co2_kg / 1000:,.1f} t |"
        )

    lines += [
        "",
        "## Highest CO2 Flights",
        "",
        "| # | Callsign | From | To | CO2 | Distance |",
        "|---:|----------|------|-----|----:|---------:|",
    ]
    for idx, r in enumerate(highest_co2, 1):
        dep = f"{r.dep_airport_name} ({r.dep_airport_icao})"
        arr = f"{r.arr_airport_name} ({r.arr_airport_icao})"
        lines.append(
            f"| {idx} | {r.callsign} | {dep} | {arr} | "
            f"{r.co2_kg / 1000:,.1f} t | {r.distance_km:,.0f} km |"
        )

    lines += [
        "",
        "---",
        "",
        f"*Based on {len(routes):,} archived flights*",
        "",
    ]

    with open(LEADERBOARD_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Leaderboard written to {LEADERBOARD_PATH}")
