"""Generate POST.txt with a Twitter/X thread about global air traffic."""

from datetime import datetime, timezone

from flights.ReadMe import COUNTRY_FLAGS, _flag


class Post:
    """Generates POST.txt with a Twitter/X thread in plain text format."""

    POST_PATH = "POST.txt"

    def __init__(self, summary: dict):
        self.summary = summary

    def _top_airlines(self, n: int = 10) -> str:
        airlines = self.summary.get("airlines", {})
        lines = []
        for idx, (airline, count) in enumerate(
            sorted(airlines.items(), key=lambda x: -x[1])[:n], 1
        ):
            lines.append(f"{idx}. {airline}: {count} aircraft")
        return "\n".join(lines)

    def _top_countries(self, n: int = 10) -> str:
        countries = self.summary.get("countries", {})
        lines = []
        for idx, (country, count) in enumerate(
            sorted(countries.items(), key=lambda x: -x[1])[:n], 1
        ):
            lines.append(f"{idx}. {_flag(country)} {country}: {count}")
        return "\n".join(lines)

    def _top_airports(self, n: int = 10) -> str:
        airports = self.summary.get("top_airports", [])
        lines = []
        for idx, ap in enumerate(airports[:n], 1):
            lines.append(
                f"{idx}. {ap['name']} ({ap['icao']}), "
                f"{ap['city']}: {ap['count']} aircraft"
            )
        return "\n".join(lines)

    def _generate_thread(self) -> str:
        ts = self.summary.get("timestamp", 0)
        dt = datetime.fromtimestamp(ts, timezone.utc)
        time_str = dt.strftime("%Y-%m-%d %H:%M UTC")

        total = self.summary.get("total_aircraft", 0)
        in_air = self.summary.get("in_air", 0)
        n_countries = len(self.summary.get("countries", {}))
        n_airports = len(self.summary.get("top_airports", []))
        n_airlines = len(self.summary.get("airlines", {}))

        lines = []

        # Tweet 1: Introduction
        lines.append("1/ Global Air Traffic - Live Snapshot")
        lines.append("")
        lines.append(f"As of {time_str}:")
        lines.append("")
        lines.append(f"- {total:,} aircraft tracked worldwide")
        lines.append(f"- {in_air:,} currently in the air")
        lines.append(f"- {n_countries} countries")
        lines.append(f"- {n_airports} airports with ground traffic")
        lines.append(f"- {n_airlines} airlines identified")
        lines.append("")
        lines.append("#Aviation #FlightTracking #OpenData")
        lines.append("")
        lines.append("---")
        lines.append("")

        # Tweet 2: Airlines
        lines.append("2/ Top Airlines by Aircraft Count")
        lines.append("")
        lines.append(self._top_airlines(10))
        lines.append("")
        lines.append("#Airlines #AviationIndustry")
        lines.append("")
        lines.append("---")
        lines.append("")

        # Tweet 3: Countries
        lines.append("3/ Top Countries by Registered Aircraft")
        lines.append("")
        lines.append(self._top_countries(10))
        lines.append("")
        lines.append("#GlobalAviation")
        lines.append("")
        lines.append("---")
        lines.append("")

        # Tweet 4: Airports
        lines.append("4/ Busiest Airports Right Now")
        lines.append("")
        lines.append(self._top_airports(10))
        lines.append("")
        lines.append("#Airports #AirTraffic")
        lines.append("")
        lines.append("---")
        lines.append("")

        # Tweet 5: About
        lines.append("5/ About This Data")
        lines.append("")
        lines.append(
            "Live data from OpenSky Network - a free, community-driven "
            "flight tracking platform."
        )
        lines.append("")
        lines.append(
            "This dataset updates automatically every 5 minutes via "
            "GitHub Actions. Aircraft are mapped to 28,000+ airports "
            "worldwide."
        )
        lines.append("")
        lines.append("Data: https://opensky-network.org/")
        lines.append(
            "Map: https://github.com/gajarthan/global_air_traffic/blob/main/"
            "images/flight_map.png"
        )
        lines.append("GitHub: https://github.com/gajarthan/global_air_traffic")
        lines.append("")
        lines.append("#OpenSky #DataScience #OpenSource")
        lines.append("")

        return "\n".join(lines)

    def write(self):
        content = self._generate_thread()
        with open(self.POST_PATH, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"POST.txt updated")
