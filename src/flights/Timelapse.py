"""Generate an animated GIF showing routes accumulating over time."""

import os
import tempfile
from collections import defaultdict
from datetime import datetime, timezone

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
from PIL import Image

from flights.Flight import FlightRoute


GIF_PATH = os.path.join("images", "timelapse.gif")


def _bucket_routes_by_hour(
    routes: list[FlightRoute],
) -> dict[str, list[FlightRoute]]:
    """Group routes into hourly buckets by departure time."""
    buckets: dict[str, list[FlightRoute]] = defaultdict(list)
    for r in routes:
        dt = datetime.fromtimestamp(r.first_seen, timezone.utc)
        key = dt.strftime("%Y-%m-%d %H:00")
        buckets[key].append(r)
    return dict(sorted(buckets.items()))


def _render_frame(
    cumulative_routes: list[FlightRoute],
    hour_label: str,
    frame_num: int,
    total_frames: int,
    path: str,
) -> None:
    """Render a single map frame showing cumulative routes."""
    fig = plt.figure(figsize=(12, 6), facecolor="#0a0e27")
    ax = plt.axes(projection=ccrs.Robinson())
    ax.set_global()
    ax.set_facecolor("#0a0e27")

    ax.add_feature(cfeature.LAND, facecolor="#1a1f3a", edgecolor="none")
    ax.add_feature(cfeature.OCEAN, facecolor="#0a0e27")
    ax.add_feature(cfeature.COASTLINE, linewidth=0.3, edgecolor="#2a3050")

    # Draw all cumulative routes
    if cumulative_routes:
        for r in cumulative_routes:
            if (
                r.dep_lat is not None and r.dep_lon is not None
                and r.arr_lat is not None and r.arr_lon is not None
            ):
                ax.plot(
                    [r.dep_lon, r.arr_lon],
                    [r.dep_lat, r.arr_lat],
                    color="#ff6b9d",
                    alpha=0.15,
                    linewidth=0.4,
                    transform=ccrs.Geodetic(),
                    zorder=1,
                )

    # Title
    ax.text(
        0.5, 0.96,
        "Global Flight Routes - Timelapse",
        transform=ax.transAxes,
        fontsize=16,
        fontweight="bold",
        color="#ffffff",
        ha="center",
        va="top",
    )

    # Subtitle with hour and count
    ax.text(
        0.5, 0.90,
        f"{hour_label} | {len(cumulative_routes):,} flights | "
        f"Frame {frame_num}/{total_frames}",
        transform=ax.transAxes,
        fontsize=9,
        color="#8899bb",
        ha="center",
        va="top",
    )

    plt.tight_layout()
    plt.savefig(path, dpi=100, facecolor="#0a0e27", bbox_inches="tight")
    plt.close()


def generate(max_frames: int = 48) -> None:
    """Generate timelapse GIF from archived routes.

    Args:
        max_frames: Maximum frames in the GIF. If there are more hourly
                    buckets than this, evenly sample them.
    """
    routes = FlightRoute.load_saved_routes()
    if not routes:
        print("No routes found, skipping timelapse.")
        return

    buckets = _bucket_routes_by_hour(routes)
    hours = list(buckets.keys())

    if not hours:
        print("No hourly buckets, skipping timelapse.")
        return

    # Sample if too many hours
    if len(hours) > max_frames:
        step = len(hours) / max_frames
        sampled = [hours[int(i * step)] for i in range(max_frames)]
        hours = sampled

    print(f"Generating {len(hours)} frames for timelapse...")

    # Build cumulative route list for each frame
    all_routes_so_far: list[FlightRoute] = []
    frames: list[str] = []

    with tempfile.TemporaryDirectory() as tmpdir:
        bucket_keys = list(buckets.keys())
        hour_set = set(hours)
        frame_idx = 0

        for key in bucket_keys:
            all_routes_so_far.extend(buckets[key])
            if key in hour_set:
                frame_idx += 1
                frame_path = os.path.join(tmpdir, f"frame_{frame_idx:04d}.png")
                _render_frame(
                    all_routes_so_far,
                    key,
                    frame_idx,
                    len(hours),
                    frame_path,
                )
                frames.append(frame_path)
                print(f"  Frame {frame_idx}/{len(hours)}: {key} "
                      f"({len(all_routes_so_far):,} routes)")

        if not frames:
            print("No frames generated.")
            return

        # Stitch into GIF using Pillow
        images = [Image.open(f) for f in frames]
        os.makedirs(os.path.dirname(GIF_PATH), exist_ok=True)
        images[0].save(
            GIF_PATH,
            save_all=True,
            append_images=images[1:],
            duration=300,  # 300ms per frame
            loop=0,
        )
        # Close images
        for img in images:
            img.close()

    print(f"Timelapse GIF saved to {GIF_PATH} ({len(frames)} frames)")
