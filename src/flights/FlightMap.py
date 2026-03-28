"""Generate a world map showing live global air traffic."""

import os
from datetime import datetime, timezone

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt


class FlightMap:
    """Creates a map visualization of live worldwide flights."""

    MAP_PATH = os.path.join("images", "flight_map.png")

    def __init__(self, flights: list, summary: dict):
        self.flights = flights
        self.summary = summary

    def create_map(self):
        """Create and save the global flight map."""
        in_air = [f for f in self.flights if not f.on_ground]
        top_airports = self.summary.get("top_airports", [])[:30]

        fig = plt.figure(figsize=(24, 12), facecolor="#0a0e27")
        ax = plt.axes(projection=ccrs.Robinson())
        ax.set_global()
        ax.set_facecolor("#0a0e27")

        # Map features
        ax.add_feature(
            cfeature.LAND, facecolor="#1a1f3a", edgecolor="none"
        )
        ax.add_feature(cfeature.OCEAN, facecolor="#0a0e27")
        ax.add_feature(
            cfeature.COASTLINE, linewidth=0.3, edgecolor="#2a3050"
        )
        ax.add_feature(
            cfeature.BORDERS,
            linewidth=0.2,
            edgecolor="#2a3050",
            alpha=0.4,
        )

        # Plot in-air aircraft as small dots
        if in_air:
            lons = [f.longitude for f in in_air]
            lats = [f.latitude for f in in_air]
            ax.scatter(
                lons,
                lats,
                s=0.8,
                c="#00d4ff",
                alpha=0.4,
                transform=ccrs.PlateCarree(),
                zorder=2,
                linewidths=0,
            )

        # Draw route lines for top routes
        top_routes = self.summary.get("top_routes", [])[:20]
        if top_routes:
            max_flights = max(r["flights"] for r in top_routes)
            for r in top_routes:
                if (
                    r.get("dep_lat") and r.get("dep_lon")
                    and r.get("arr_lat") and r.get("arr_lon")
                ):
                    alpha = 0.15 + (r["flights"] / max_flights) * 0.45
                    lw = 0.3 + (r["flights"] / max_flights) * 2.0
                    ax.plot(
                        [r["dep_lon"], r["arr_lon"]],
                        [r["dep_lat"], r["arr_lat"]],
                        color="#ff6b9d",
                        alpha=alpha,
                        linewidth=lw,
                        transform=ccrs.Geodetic(),
                        zorder=1,
                    )

        # Plot top airports as larger circles
        if top_airports:
            max_count = max(a["count"] for a in top_airports)
            for ap in top_airports:
                size = 20 + (ap["count"] / max_count) * 200
                alpha = 0.5 + (ap["count"] / max_count) * 0.4
                ax.scatter(
                    ap["lon"],
                    ap["lat"],
                    s=size,
                    c="#ff6b35",
                    alpha=alpha,
                    edgecolors="#ffaa00",
                    linewidths=0.5,
                    transform=ccrs.PlateCarree(),
                    zorder=3,
                )

        # Title
        ax.text(
            0.5,
            0.96,
            "Global Live Air Traffic",
            transform=ax.transAxes,
            fontsize=26,
            fontweight="bold",
            color="#ffffff",
            ha="center",
            va="top",
        )

        # Subtitle with stats
        ts = self.summary.get("timestamp", 0)
        dt = datetime.fromtimestamp(ts, timezone.utc)
        time_str = dt.strftime("%Y-%m-%d %H:%M UTC")

        total = self.summary.get("total_aircraft", 0)
        in_air_count = self.summary.get("in_air", 0)
        n_countries = len(self.summary.get("countries", {}))
        n_airports = len(self.summary.get("top_airports", []))

        ax.text(
            0.5,
            0.92,
            f"{total:,} aircraft tracked | {in_air_count:,} in air | "
            f"{n_countries} countries | {n_airports} airports | {time_str}",
            transform=ax.transAxes,
            fontsize=12,
            color="#8899bb",
            ha="center",
            va="top",
        )

        # Gridlines
        ax.gridlines(
            draw_labels=False,
            linewidth=0.3,
            color="#2a3050",
            alpha=0.3,
            linestyle="--",
        )

        # Save
        os.makedirs(os.path.dirname(self.MAP_PATH), exist_ok=True)
        plt.tight_layout()
        plt.savefig(
            self.MAP_PATH,
            dpi=150,
            facecolor="#0a0e27",
            bbox_inches="tight",
        )
        plt.close()
        print(f"Flight map saved to {self.MAP_PATH}")
