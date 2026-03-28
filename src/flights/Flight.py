"""Fetch live flight data from OpenSky Network API."""

import json
import os
import time
from collections import Counter
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Optional

import httpx

from flights.Airport import Airport

OPENSKY_STATES_URL = "https://opensky-network.org/api/states/all"
OPENSKY_FLIGHTS_URL = "https://opensky-network.org/api/flights/all"
REQUEST_TIMEOUT = 60
MAX_RETRIES = 3
RETRY_DELAY = 10

# ICAO 3-letter airline codes → airline names (top ~80 carriers)
AIRLINE_CODES = {
    "AAL": "American Airlines",
    "ACA": "Air Canada",
    "AFR": "Air France",
    "AIC": "Air India",
    "AMX": "Aeromexico",
    "ANA": "All Nippon Airways",
    "ASA": "Alaska Airlines",
    "AUA": "Austrian Airlines",
    "AVA": "Avianca",
    "AZA": "Alitalia/ITA",
    "BAW": "British Airways",
    "BEL": "Brussels Airlines",
    "CCA": "Air China",
    "CES": "China Eastern",
    "CPA": "Cathay Pacific",
    "CSN": "China Southern",
    "DAL": "Delta Air Lines",
    "DLH": "Lufthansa",
    "EIN": "Aer Lingus",
    "ETD": "Etihad Airways",
    "ETH": "Ethiopian Airlines",
    "EVA": "EVA Air",
    "EZY": "easyJet",
    "FDB": "flydubai",
    "FIN": "Finnair",
    "GFA": "Gulf Air",
    "GIA": "Garuda Indonesia",
    "HAL": "Hawaiian Airlines",
    "IBE": "Iberia",
    "IGO": "IndiGo",
    "JAL": "Japan Airlines",
    "JBU": "JetBlue",
    "KAC": "Kuwait Airways",
    "KAL": "Korean Air",
    "KLM": "KLM Royal Dutch",
    "LOT": "LOT Polish Airlines",
    "MAS": "Malaysia Airlines",
    "MEA": "Middle East Airlines",
    "MSR": "EgyptAir",
    "NOZ": "Norwegian Air",
    "OMA": "Oman Air",
    "PAL": "Philippine Airlines",
    "PIA": "Pakistan International",
    "QFA": "Qantas",
    "QTR": "Qatar Airways",
    "RAM": "Royal Air Maroc",
    "RJA": "Royal Jordanian",
    "RPA": "Republic Airways",
    "RYR": "Ryanair",
    "SAS": "Scandinavian Airlines",
    "SIA": "Singapore Airlines",
    "SKW": "SkyWest Airlines",
    "SLK": "SriLankan Airlines",
    "SVA": "Saudia",
    "SWA": "Southwest Airlines",
    "SWR": "Swiss International",
    "TAM": "LATAM Airlines",
    "TAP": "TAP Air Portugal",
    "THA": "Thai Airways",
    "THY": "Turkish Airlines",
    "UAE": "Emirates",
    "UAL": "United Airlines",
    "VIR": "Virgin Atlantic",
    "VLG": "Vueling",
    "VOZ": "Virgin Australia",
    "WZZ": "Wizz Air",
}


@dataclass
class FlightRoute:
    """A completed flight with departure and arrival airports."""

    icao24: str
    callsign: str
    dep_airport_icao: str
    dep_airport_name: str
    dep_country: str
    dep_lat: Optional[float]
    dep_lon: Optional[float]
    arr_airport_icao: str
    arr_airport_name: str
    arr_country: str
    arr_lat: Optional[float]
    arr_lon: Optional[float]
    first_seen: int
    last_seen: int
    airline: str

    @property
    def departure_time(self) -> str:
        """Formatted departure time (UTC)."""
        return datetime.fromtimestamp(
            self.first_seen, timezone.utc
        ).strftime("%Y-%m-%d %H:%M UTC")

    @property
    def arrival_time(self) -> str:
        """Formatted arrival time (UTC)."""
        return datetime.fromtimestamp(
            self.last_seen, timezone.utc
        ).strftime("%Y-%m-%d %H:%M UTC")

    @property
    def duration_minutes(self) -> int:
        """Flight duration in minutes."""
        return max(0, (self.last_seen - self.first_seen) // 60)

    @property
    def duration_str(self) -> str:
        """Flight duration as 'Xh Ym'."""
        mins = self.duration_minutes
        h, m = divmod(mins, 60)
        if h > 0:
            return f"{h}h {m}m"
        return f"{m}m"

    def to_dict(self) -> dict:
        d = asdict(self)
        d["departure_time"] = self.departure_time
        d["arrival_time"] = self.arrival_time
        d["duration_minutes"] = self.duration_minutes
        d["duration_str"] = self.duration_str
        return d

    @classmethod
    def from_dict(cls, data: dict) -> "FlightRoute":
        # Remove computed fields that aren't constructor args
        filtered = {
            k: v
            for k, v in data.items()
            if k
            not in ("departure_time", "arrival_time", "duration_minutes",
                     "duration_str")
        }
        return cls(**filtered)

    @property
    def file_name(self) -> str:
        """Generate filename: <callsign>_<dep>_<arr>_<YYYYMMDD_HHMM>.json"""
        dt = datetime.fromtimestamp(self.first_seen, timezone.utc)
        ts = dt.strftime("%Y%m%d_%H%M")
        cs = self.callsign or self.icao24
        cs = cs.replace("/", "-").replace(" ", "")
        return f"{cs}_{self.dep_airport_icao}_{self.arr_airport_icao}_{ts}.json"

    def to_json_file(self, path: str):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2)

    @classmethod
    def fetch_routes(cls, hours: int = 2) -> list["FlightRoute"]:
        """Fetch completed flights from the last N hours (requires auth)."""
        username = os.environ.get("OPENSKY_USERNAME")
        password = os.environ.get("OPENSKY_PASSWORD")
        auth = (username, password) if username and password else None

        now = int(time.time())
        begin = now - (hours * 3600)

        last_error: Optional[Exception] = None
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                resp = httpx.get(
                    OPENSKY_FLIGHTS_URL,
                    params={"begin": begin, "end": now},
                    auth=auth,
                    timeout=httpx.Timeout(REQUEST_TIMEOUT),
                )
                resp.raise_for_status()
                raw_flights = resp.json()
                break
            except (
                httpx.TimeoutException,
                httpx.NetworkError,
                httpx.HTTPStatusError,
            ) as e:
                last_error = e
                print(f"Route fetch attempt {attempt}/{MAX_RETRIES}: {e}")
                if attempt < MAX_RETRIES:
                    time.sleep(RETRY_DELAY * attempt)
        else:
            print(
                f"Warning: Could not fetch routes ({last_error}). "
                "Routes require OpenSky auth (free registration)."
            )
            return []

        airports_db = Airport.load_all()
        routes = []
        for r in raw_flights:
            dep_icao = r.get("estDepartureAirport") or ""
            arr_icao = r.get("estArrivalAirport") or ""
            if not dep_icao or not arr_icao:
                continue

            dep_ap = airports_db.get(dep_icao)
            arr_ap = airports_db.get(arr_icao)

            callsign = (r.get("callsign") or "").strip()
            code = "".join(c for c in callsign[:3] if c.isalpha())
            airline = AIRLINE_CODES.get(code, code) if len(code) == 3 else ""

            routes.append(
                cls(
                    icao24=r.get("icao24", ""),
                    callsign=callsign,
                    dep_airport_icao=dep_icao,
                    dep_airport_name=dep_ap.name if dep_ap else dep_icao,
                    dep_country=dep_ap.country if dep_ap else "",
                    dep_lat=dep_ap.latitude if dep_ap else None,
                    dep_lon=dep_ap.longitude if dep_ap else None,
                    arr_airport_icao=arr_icao,
                    arr_airport_name=arr_ap.name if arr_ap else arr_icao,
                    arr_country=arr_ap.country if arr_ap else "",
                    arr_lat=arr_ap.latitude if arr_ap else None,
                    arr_lon=arr_ap.longitude if arr_ap else None,
                    first_seen=r.get("firstSeen", 0),
                    last_seen=r.get("lastSeen", 0),
                    airline=airline,
                )
            )

        print(f"Fetched {len(routes)} flight routes (last {hours}h)")
        return routes

    @classmethod
    def save_routes(cls, routes: list["FlightRoute"]) -> None:
        """Save individual route files and aggregated routes.json."""
        flights_dir = os.path.join("data", "flights")
        os.makedirs(flights_dir, exist_ok=True)

        for route in routes:
            route.to_json_file(os.path.join(flights_dir, route.file_name))

        agg_path = os.path.join("data", "routes.json")
        with open(agg_path, "w", encoding="utf-8") as f:
            json.dump([r.to_dict() for r in routes], f, indent=2)

        print(
            f"Saved {len(routes)} route files to data/flights/ "
            f"and data/routes.json"
        )


@dataclass
class Flight:
    icao24: str
    callsign: str
    origin_country: str
    longitude: float
    latitude: float
    altitude: float
    velocity: float
    heading: float
    on_ground: bool
    timestamp: int
    nearest_airport_icao: Optional[str] = None
    nearest_airport_name: Optional[str] = None

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Flight":
        return cls(**data)

    @property
    def airline_code(self) -> str:
        """Extract 3-letter ICAO airline code from callsign."""
        if self.callsign and len(self.callsign) >= 3:
            prefix = "".join(c for c in self.callsign[:3] if c.isalpha())
            if len(prefix) == 3:
                return prefix
        return ""

    @property
    def airline_name(self) -> str:
        """Resolve airline name from callsign code."""
        code = self.airline_code
        return AIRLINE_CODES.get(code, code)

    @classmethod
    def fetch_live(cls) -> list["Flight"]:
        """Fetch all live aircraft from OpenSky Network."""
        username = os.environ.get("OPENSKY_USERNAME")
        password = os.environ.get("OPENSKY_PASSWORD")
        auth = (username, password) if username and password else None

        last_error: Optional[Exception] = None
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                resp = httpx.get(
                    OPENSKY_STATES_URL,
                    auth=auth,
                    timeout=httpx.Timeout(REQUEST_TIMEOUT),
                )
                resp.raise_for_status()
                data = resp.json()

                flights = []
                ts = data.get("time", int(time.time()))
                for s in data.get("states") or []:
                    if s[5] is None or s[6] is None:
                        continue
                    flights.append(
                        cls(
                            icao24=s[0] or "",
                            callsign=(s[1] or "").strip(),
                            origin_country=s[2] or "",
                            longitude=s[5],
                            latitude=s[6],
                            altitude=s[7] or 0.0,
                            velocity=s[9] or 0.0,
                            heading=s[10] or 0.0,
                            on_ground=bool(s[8]),
                            timestamp=ts,
                        )
                    )

                # Map on-ground aircraft to nearest airports
                for f in flights:
                    if f.on_ground:
                        ap = Airport.find_nearest(f.latitude, f.longitude)
                        if ap:
                            f.nearest_airport_icao = ap.icao
                            f.nearest_airport_name = ap.name

                print(
                    f"Fetched {len(flights)} aircraft "
                    f"({sum(1 for f in flights if not f.on_ground)} in air, "
                    f"{sum(1 for f in flights if f.on_ground)} on ground)"
                )
                return flights

            except (
                httpx.TimeoutException,
                httpx.NetworkError,
                httpx.HTTPStatusError,
            ) as e:
                last_error = e
                print(
                    f"Attempt {attempt}/{MAX_RETRIES} failed: {e}"
                )
                if attempt < MAX_RETRIES:
                    time.sleep(RETRY_DELAY * attempt)

        raise RuntimeError(
            f"Failed to fetch flights after {MAX_RETRIES} attempts: "
            f"{last_error}"
        )

    @classmethod
    def compute_summary(
        cls,
        flights: list["Flight"],
        routes: list["FlightRoute"] | None = None,
    ) -> dict:
        """Compute summary statistics from live flights and routes."""
        in_air = [f for f in flights if not f.on_ground]
        on_ground = [f for f in flights if f.on_ground]

        # Country stats (registration country of aircraft)
        country_counts = Counter(
            f.origin_country for f in flights if f.origin_country
        )

        # Airport stats (from on-ground aircraft)
        airport_counts: Counter = Counter()
        airport_info: dict = {}
        airports_db = Airport.load_all()

        for f in on_ground:
            if f.nearest_airport_icao:
                airport_counts[f.nearest_airport_icao] += 1
                if f.nearest_airport_icao not in airport_info:
                    ap = airports_db.get(f.nearest_airport_icao)
                    if ap:
                        airport_info[f.nearest_airport_icao] = {
                            "name": ap.name,
                            "city": ap.city,
                            "country": ap.country,
                            "lat": ap.latitude,
                            "lon": ap.longitude,
                        }

        top_airports = []
        for icao, count in airport_counts.most_common(100):
            if icao in airport_info:
                top_airports.append(
                    {**airport_info[icao], "icao": icao, "count": count}
                )

        # Airline stats (from callsign prefixes)
        airline_counts: Counter = Counter()
        for f in flights:
            code = f.airline_code
            if code:
                name = AIRLINE_CODES.get(code, code)
                airline_counts[name] += 1

        # Route stats (from /flights/all)
        top_routes: list[dict] = []
        recent_flights: list[dict] = []
        route_count = 0
        avg_duration = 0
        if routes:
            route_count = len(routes)

            # Average flight duration
            durations = [r.duration_minutes for r in routes if r.duration_minutes > 0]
            avg_duration = round(sum(durations) / len(durations)) if durations else 0

            # Top routes with avg duration
            route_pairs: Counter = Counter()
            route_details: dict = {}
            route_durations: dict[str, list[int]] = {}
            for r in routes:
                key = f"{r.dep_airport_icao}-{r.arr_airport_icao}"
                route_pairs[key] += 1
                route_durations.setdefault(key, []).append(r.duration_minutes)
                if key not in route_details:
                    route_details[key] = {
                        "dep_icao": r.dep_airport_icao,
                        "dep_name": r.dep_airport_name,
                        "dep_country": r.dep_country,
                        "dep_lat": r.dep_lat,
                        "dep_lon": r.dep_lon,
                        "arr_icao": r.arr_airport_icao,
                        "arr_name": r.arr_airport_name,
                        "arr_country": r.arr_country,
                        "arr_lat": r.arr_lat,
                        "arr_lon": r.arr_lon,
                    }
            for key, count in route_pairs.most_common(50):
                durs = route_durations[key]
                avg_dur = round(sum(durs) / len(durs)) if durs else 0
                h, m = divmod(avg_dur, 60)
                dur_str = f"{h}h {m}m" if h > 0 else f"{m}m"
                top_routes.append(
                    {**route_details[key], "flights": count,
                     "avg_duration_min": avg_dur, "avg_duration": dur_str}
                )

            # Recent flights (last 20, sorted by arrival time)
            sorted_routes = sorted(routes, key=lambda r: r.last_seen, reverse=True)
            for r in sorted_routes[:20]:
                recent_flights.append({
                    "callsign": r.callsign,
                    "airline": r.airline,
                    "from": f"{r.dep_airport_name} ({r.dep_airport_icao})",
                    "to": f"{r.arr_airport_name} ({r.arr_airport_icao})",
                    "departure": r.departure_time,
                    "arrival": r.arrival_time,
                    "duration": r.duration_str,
                })

        # Overall avg duration string
        avg_h, avg_m = divmod(avg_duration, 60)
        avg_dur_str = f"{avg_h}h {avg_m}m" if avg_h > 0 else f"{avg_m}m"

        return {
            "timestamp": (
                flights[0].timestamp if flights else int(time.time())
            ),
            "total_aircraft": len(flights),
            "in_air": len(in_air),
            "on_ground": len(on_ground),
            "countries": dict(country_counts.most_common()),
            "top_airports": top_airports,
            "airlines": dict(airline_counts.most_common(50)),
            "route_count": route_count,
            "avg_duration": avg_dur_str,
            "avg_duration_min": avg_duration,
            "top_routes": top_routes,
            "recent_flights": recent_flights,
        }
