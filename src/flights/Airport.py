"""Airport metadata using airportsdata package (28,000+ airports worldwide)."""

from dataclasses import dataclass
from functools import lru_cache
from math import asin, cos, radians, sin, sqrt

import airportsdata


def _haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Distance in km between two lat/lon points."""
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    return 2 * 6371 * asin(sqrt(a))


@dataclass
class Airport:
    icao: str
    name: str
    city: str
    country: str
    latitude: float
    longitude: float

    @classmethod
    @lru_cache(maxsize=1)
    def _load_all(cls) -> dict[str, "Airport"]:
        raw = airportsdata.load("ICAO")
        return {
            code: cls(
                icao=code,
                name=info["name"],
                city=info.get("city", ""),
                country=info.get("country", ""),
                latitude=info["lat"],
                longitude=info["lon"],
            )
            for code, info in raw.items()
            if info.get("lat") and info.get("lon")
        }

    @classmethod
    @lru_cache(maxsize=1)
    def _build_grid(cls) -> dict[tuple[int, int], list["Airport"]]:
        """Spatial grid (1-degree cells) for fast nearest-airport lookups."""
        grid: dict[tuple[int, int], list["Airport"]] = {}
        for ap in cls._load_all().values():
            key = (round(ap.latitude), round(ap.longitude))
            grid.setdefault(key, []).append(ap)
        return grid

    @classmethod
    def load_all(cls) -> dict[str, "Airport"]:
        return cls._load_all()

    @classmethod
    def find_nearest(
        cls, lat: float, lon: float, max_km: float = 5.0
    ) -> "Airport | None":
        """Find nearest airport within max_km using spatial grid."""
        grid = cls._build_grid()
        rlat, rlon = round(lat), round(lon)

        best = None
        best_dist = max_km

        for dlat in (-1, 0, 1):
            for dlon in (-1, 0, 1):
                for ap in grid.get((rlat + dlat, rlon + dlon), []):
                    dist = _haversine_km(
                        lat, lon, ap.latitude, ap.longitude
                    )
                    if dist < best_dist:
                        best_dist = dist
                        best = ap

        return best
