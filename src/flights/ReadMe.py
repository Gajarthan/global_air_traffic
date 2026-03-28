"""Generate README.md with global air traffic statistics."""

from datetime import datetime, timezone

COUNTRY_FLAGS = {
    "Argentina": "\U0001f1e6\U0001f1f7",
    "Australia": "\U0001f1e6\U0001f1fa",
    "Austria": "\U0001f1e6\U0001f1f9",
    "Bangladesh": "\U0001f1e7\U0001f1e9",
    "Belgium": "\U0001f1e7\U0001f1ea",
    "Brazil": "\U0001f1e7\U0001f1f7",
    "Canada": "\U0001f1e8\U0001f1e6",
    "Chile": "\U0001f1e8\U0001f1f1",
    "China": "\U0001f1e8\U0001f1f3",
    "Colombia": "\U0001f1e8\U0001f1f4",
    "Denmark": "\U0001f1e9\U0001f1f0",
    "Egypt": "\U0001f1ea\U0001f1ec",
    "Ethiopia": "\U0001f1ea\U0001f1f9",
    "Finland": "\U0001f1eb\U0001f1ee",
    "France": "\U0001f1eb\U0001f1f7",
    "Germany": "\U0001f1e9\U0001f1ea",
    "Hong Kong": "\U0001f1ed\U0001f1f0",
    "India": "\U0001f1ee\U0001f1f3",
    "Indonesia": "\U0001f1ee\U0001f1e9",
    "Ireland": "\U0001f1ee\U0001f1ea",
    "Israel": "\U0001f1ee\U0001f1f1",
    "Italy": "\U0001f1ee\U0001f1f9",
    "Japan": "\U0001f1ef\U0001f1f5",
    "Kenya": "\U0001f1f0\U0001f1ea",
    "Kuwait": "\U0001f1f0\U0001f1fc",
    "Malaysia": "\U0001f1f2\U0001f1fe",
    "Mexico": "\U0001f1f2\U0001f1fd",
    "Netherlands": "\U0001f1f3\U0001f1f1",
    "New Zealand": "\U0001f1f3\U0001f1ff",
    "Nigeria": "\U0001f1f3\U0001f1ec",
    "Norway": "\U0001f1f3\U0001f1f4",
    "Oman": "\U0001f1f4\U0001f1f2",
    "Pakistan": "\U0001f1f5\U0001f1f0",
    "Peru": "\U0001f1f5\U0001f1ea",
    "Philippines": "\U0001f1f5\U0001f1ed",
    "Poland": "\U0001f1f5\U0001f1f1",
    "Portugal": "\U0001f1f5\U0001f1f9",
    "Qatar": "\U0001f1f6\U0001f1e6",
    "Russia": "\U0001f1f7\U0001f1fa",
    "Saudi Arabia": "\U0001f1f8\U0001f1e6",
    "Singapore": "\U0001f1f8\U0001f1ec",
    "South Africa": "\U0001f1ff\U0001f1e6",
    "South Korea": "\U0001f1f0\U0001f1f7",
    "Spain": "\U0001f1ea\U0001f1f8",
    "Sri Lanka": "\U0001f1f1\U0001f1f0",
    "Sweden": "\U0001f1f8\U0001f1ea",
    "Switzerland": "\U0001f1e8\U0001f1ed",
    "Taiwan": "\U0001f1f9\U0001f1fc",
    "Thailand": "\U0001f1f9\U0001f1ed",
    "Turkey": "\U0001f1f9\U0001f1f7",
    "United Arab Emirates": "\U0001f1e6\U0001f1ea",
    "United Kingdom": "\U0001f1ec\U0001f1e7",
    "United States": "\U0001f1fa\U0001f1f8",
    "Vietnam": "\U0001f1fb\U0001f1f3",
}


def _flag(country: str) -> str:
    return COUNTRY_FLAGS.get(country, "\U0001f3f3\ufe0f")


class ReadMe:
    """Generates README.md with global air traffic stats."""

    README_PATH = "README.md"

    def __init__(self, summary: dict):
        self.summary = summary

    def _airline_table(self) -> list[str]:
        airlines = self.summary.get("airlines", {})
        lines = [
            "## Top Airlines",
            "",
            "| # | Airline | Aircraft |",
            "|---:|---------|--------:|",
        ]
        for idx, (airline, count) in enumerate(
            sorted(airlines.items(), key=lambda x: -x[1])[:30], 1
        ):
            lines.append(f"| {idx} | {airline} | {count} |")
        return lines

    def _country_table(self) -> list[str]:
        countries = self.summary.get("countries", {})
        lines = [
            "## Top Countries (by aircraft registration)",
            "",
            "| # | Country | Aircraft |",
            "|---:|---------|--------:|",
        ]
        for idx, (country, count) in enumerate(
            sorted(countries.items(), key=lambda x: -x[1])[:30], 1
        ):
            lines.append(f"| {idx} | {_flag(country)} {country} | {count} |")
        return lines

    def _airport_table(self) -> list[str]:
        airports = self.summary.get("top_airports", [])
        lines = [
            "## Busiest Airports (aircraft on ground)",
            "",
            "| # | Airport | City | Country | Aircraft |",
            "|---:|---------|------|---------|--------:|",
        ]
        for idx, ap in enumerate(airports[:40], 1):
            lines.append(
                f"| {idx} | {ap['name']} | {ap['city']} | "
                f"{ap['country']} | {ap['count']} |"
            )
        return lines

    def _route_table(self) -> list[str]:
        routes = self.summary.get("top_routes", [])
        if not routes:
            return []
        lines = [
            "## Top Routes (last 2 hours)",
            "",
            "| # | From | To | Flights | Avg Duration |",
            "|---:|------|-----|--------:|------------:|",
        ]
        for idx, r in enumerate(routes[:30], 1):
            dep = f"{r['dep_name']} ({r['dep_icao']})"
            arr = f"{r['arr_name']} ({r['arr_icao']})"
            dur = r.get('avg_duration', '-')
            lines.append(f"| {idx} | {dep} | {arr} | {r['flights']} | {dur} |")
        return lines

    def _recent_flights_table(self) -> list[str]:
        flights = self.summary.get("recent_flights", [])
        if not flights:
            return []
        lines = [
            "## Recent Flights",
            "",
            "| Callsign | Airline | From | To | Departure | Arrival | Duration |",
            "|----------|---------|------|-----|-----------|---------|----------|",
        ]
        for f in flights:
            lines.append(
                f"| {f['callsign']} | {f['airline']} | {f['from']} | "
                f"{f['to']} | {f['departure']} | {f['arrival']} | {f['duration']} |"
            )
        return lines

    def _build_md(self) -> str:
        ts = self.summary.get("timestamp", 0)
        dt = datetime.fromtimestamp(ts, timezone.utc)
        timestamp = dt.strftime("%Y--%m--%d_%H:%M:%S_UTC")
        time_display = dt.strftime("%Y-%m-%d %H:%M:%S UTC")

        total = self.summary.get("total_aircraft", 0)
        in_air = self.summary.get("in_air", 0)
        on_ground = self.summary.get("on_ground", 0)
        n_countries = len(self.summary.get("countries", {}))
        n_airports = len(self.summary.get("top_airports", []))
        n_airlines = len(self.summary.get("airlines", {}))

        lines = [
            "# Global Air Traffic Tracker",
            "",
            f"![LastUpdated](https://img.shields.io/badge/last_updated-{timestamp}-green)",
            "",
            "![Flight Map](images/flight_map.png)",
            "",
            "## About",
            "",
            "Real-time tracking of global air traffic using the "
            "[OpenSky Network](https://opensky-network.org/) API. "
            "This repository automatically fetches live aircraft positions "
            "worldwide and generates visualizations and statistics.",
            "",
            "**Data Source:** OpenSky Network REST API (`/states/all`)",
            "",
            "**Update Frequency:** Every 5 minutes via GitHub Actions",
            "",
            "**How it works:**",
            "- Fetches all aircraft transponder data globally",
            "- Maps on-ground aircraft to nearest airports "
            "(28,000+ airport database)",
            "- Identifies airlines from ICAO callsign prefixes",
            "- Generates a live flight map and summary statistics",
            "",
            "## Live Snapshot",
            "",
            f"**{time_display}**",
            "",
            f"- **{total:,}** aircraft tracked",
            f"- **{in_air:,}** currently in the air",
            f"- **{on_ground:,}** on the ground",
            f"- **{n_countries}** countries",
            f"- **{n_airports}** airports with traffic",
            f"- **{n_airlines}** airlines identified",
        ]
        route_count = self.summary.get("route_count", 0)
        if route_count:
            avg_dur = self.summary.get("avg_duration", "")
            lines.append(f"- **{route_count:,}** flight routes (last 2h)")
            if avg_dur:
                lines.append(f"- **{avg_dur}** average flight duration")
        lines.append("")

        lines += self._airline_table()
        lines.append("")
        lines += self._country_table()
        lines.append("")
        lines += self._airport_table()
        route_lines = self._route_table()
        if route_lines:
            lines.append("")
            lines += route_lines
        recent_lines = self._recent_flights_table()
        if recent_lines:
            lines.append("")
            lines += recent_lines
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append(
            "![MadeWith](https://img.shields.io/badge/made_with-python-blue)"
        )
        lines.append(
            "[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]"
            "(https://opensource.org/licenses/MIT)"
        )
        lines.append(
            "[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)]"
            "(https://opensky-network.org/)"
        )
        lines.append("")
        return "\n".join(lines)

    def write(self):
        md = self._build_md()
        with open(self.README_PATH, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"README.md updated")
