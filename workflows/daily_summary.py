"""Daily workflow: generate daily report and timelapse GIF."""

from flights.DailyReport import generate as generate_report
from flights.Timelapse import generate as generate_timelapse

if __name__ == "__main__":
    generate_report()
    generate_timelapse()
