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
    if len(country) == 2 and country.isalpha():
        country = country.upper()
        return "".join(chr(127397 + ord(char)) for char in country)
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
        heading = "## Top Countries (by aircraft registration)"
        value_label = "Aircraft"
        if self.summary.get("mode") == "historical":
            heading = "## Top Countries (by route endpoints)"
            value_label = "Flights"
        lines = [
            heading,
            "",
            f"| # | Country | {value_label} |",
            "|---:|---------|--------:|",
        ]
        for idx, (country, count) in enumerate(
            sorted(countries.items(), key=lambda x: -x[1])[:30], 1
        ):
            lines.append(f"| {idx} | {_flag(country)} {country} | {count} |")
        return lines

    def _airport_table(self) -> list[str]:
        airports = self.summary.get("top_airports", [])
        heading = "## Busiest Airports (aircraft on ground)"
        value_label = "Aircraft"
        if self.summary.get("mode") == "historical":
            heading = "## Busiest Airports (departures + arrivals across archive)"
            value_label = "Flights"
        lines = [
            heading,
            "",
            f"| # | Airport | City | Country | {value_label} |",
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
        heading = "## Top Routes (last 2 hours)"
        if self.summary.get("mode") == "historical":
            heading = "## Top Routes (all saved history)"
        lines = [
            heading,
            "",
            "| # | From | To | Flights | Avg Duration | Distance | CO2 |",
            "|---:|------|-----|--------:|------------:|--------:|----:|",
        ]
        for idx, r in enumerate(routes[:30], 1):
            dep = f"{r['dep_name']} ({r['dep_icao']})"
            arr = f"{r['arr_name']} ({r['arr_icao']})"
            dur = r.get('avg_duration', '-')
            dist = r.get('distance_km', 0)
            dist_str = f"{dist:,.0f} km" if dist else "-"
            co2 = r.get('total_co2_kg', 0)
            co2_str = f"{co2 / 1000:,.1f} t" if co2 else "-"
            lines.append(f"| {idx} | {dep} | {arr} | {r['flights']} | {dur} | {dist_str} | {co2_str} |")
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
        mode = self.summary.get("mode", "live")
        ts = self.summary.get("timestamp", 0)
        dt = datetime.fromtimestamp(ts, timezone.utc)
        timestamp = dt.strftime("%Y--%m--%d_%H:%M:%S_UTC")
        time_display = dt.strftime("%Y-%m-%d %H:%M:%S UTC")

        n_countries = len(self.summary.get("countries", {}))
        n_airports = len(self.summary.get("top_airports", []))
        n_airlines = len(self.summary.get("airlines", {}))

        if mode == "historical":
            start_ts = self.summary.get("archive_start", 0)
            end_ts = self.summary.get("archive_end", ts)
            start_display = datetime.fromtimestamp(
                start_ts, timezone.utc
            ).strftime("%Y-%m-%d %H:%M:%S UTC")
            end_display = datetime.fromtimestamp(
                end_ts, timezone.utc
            ).strftime("%Y-%m-%d %H:%M:%S UTC")
            total_flights = self.summary.get("total_flights", 0)
            unique_routes = self.summary.get("unique_routes", 0)

            lines = [
                "# Global Air Traffic Tracker",
                "",
                f"![LastUpdated](https://img.shields.io/badge/last_updated-{timestamp}-green)",
                "",
                "![Flight Map](images/flight_map.png)",
                "",
                "## About",
                "",
                "Historical archive of saved air traffic routes collected from the "
                "[OpenSky Network](https://opensky-network.org/) API. "
                "This repository keeps appending completed flights to "
                "`data/flights/` and rebuilds the visuals from the full archive.",
                "",
                "**Data Source:** Saved route files in `data/flights/` "
                "(originally fetched from OpenSky `/flights/all`)",
                "",
                "**Update Frequency:** Every 5 minutes via GitHub Actions",
                "",
                "**How it works:**",
                "- Fetches recently completed routes from OpenSky",
                "- Saves each route as a JSON file in `data/flights/`",
                "- Rebuilds aggregate statistics from all saved historical routes",
                "- Generates a historical route map and archive summary",
                "- Generates daily reports, weekly leaderboards, and timelapse GIFs",
                "",
                "## Route Timelapse",
                "",
                "![Timelapse](images/timelapse.gif)",
                "",
                "## Archive Snapshot",
                "",
                f"**Latest saved flight:** {time_display}",
                f"**Archive range:** {start_display} to {end_display}",
                "",
                f"- **{total_flights:,}** saved flights",
                f"- **{unique_routes:,}** unique routes",
                f"- **{n_countries}** countries touched by saved routes",
                f"- **{n_airports}** airports in the archive",
                f"- **{n_airlines}** airlines identified",
            ]
        else:
            total = self.summary.get("total_aircraft", 0)
            in_air = self.summary.get("in_air", 0)
            on_ground = self.summary.get("on_ground", 0)
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
            route_label = "flight routes (last 2h)"
            if mode == "historical":
                route_label = "saved routes in the archive"
            lines.append(f"- **{route_count:,}** {route_label}")
            if avg_dur:
                lines.append(f"- **{avg_dur}** average flight duration")

        # Carbon emissions stats
        total_co2 = self.summary.get("total_co2_tonnes", 0)
        avg_dist = self.summary.get("avg_distance_km", 0)
        total_dist = self.summary.get("total_distance_km", 0)
        if total_co2 > 0:
            lines.append("")
            lines.append("### Carbon Footprint Estimate")
            lines.append("")
            lines.append(
                f"- **{total_co2:,.1f} tonnes** estimated CO2 emissions"
            )
            lines.append(
                f"- **{total_dist:,.0f} km** total distance flown"
            )
            lines.append(
                f"- **{avg_dist:,.0f} km** average flight distance"
            )
            lines.append(
                "*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*"
            )
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
