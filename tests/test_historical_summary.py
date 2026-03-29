import os
import tempfile
import unittest

from flights.Flight import Flight, FlightRoute


def make_route(**overrides):
    base = {
        "icao24": "abc123",
        "callsign": "UAL100",
        "dep_airport_icao": "KJFK",
        "dep_airport_name": "John F Kennedy International Airport",
        "dep_country": "United States",
        "dep_lat": 40.6413,
        "dep_lon": -73.7781,
        "arr_airport_icao": "KLAX",
        "arr_airport_name": "Los Angeles International Airport",
        "arr_country": "United States",
        "arr_lat": 33.9416,
        "arr_lon": -118.4085,
        "first_seen": 1_700_000_000,
        "last_seen": 1_700_000_600,
        "airline": "United Airlines",
    }
    base.update(overrides)
    return FlightRoute(**base)


class HistoricalSummaryTests(unittest.TestCase):
    def test_load_saved_routes_reads_archived_json_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            route = make_route()
            route.to_json_file(os.path.join(temp_dir, "route.json"))

            loaded = FlightRoute.load_saved_routes(temp_dir)

        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].callsign, "UAL100")
        self.assertEqual(loaded[0].arr_airport_icao, "KLAX")

    def test_compute_historical_summary_aggregates_all_saved_routes(self):
        routes = [
            make_route(last_seen=1_700_000_600),
            make_route(
                callsign="DAL200",
                airline="Delta Air Lines",
                dep_airport_icao="KATL",
                dep_airport_name="Hartsfield/Jackson Atlanta International Airport",
                arr_airport_icao="KMIA",
                arr_airport_name="Miami International Airport",
                arr_country="United States",
                dep_lat=33.6407,
                dep_lon=-84.4277,
                arr_lat=25.7959,
                arr_lon=-80.2870,
                first_seen=1_700_001_000,
                last_seen=1_700_001_900,
            ),
            make_route(
                callsign="UAL101",
                dep_airport_icao="KJFK",
                dep_airport_name="John F Kennedy International Airport",
                arr_airport_icao="KLAX",
                arr_airport_name="Los Angeles International Airport",
                first_seen=1_700_002_000,
                last_seen=1_700_002_720,
            ),
        ]

        summary = Flight.compute_historical_summary(routes)

        self.assertEqual(summary["mode"], "historical")
        self.assertEqual(summary["total_flights"], 3)
        self.assertEqual(summary["route_count"], 3)
        self.assertEqual(summary["unique_routes"], 2)
        self.assertEqual(summary["airlines"]["United Airlines"], 2)
        self.assertEqual(summary["top_routes"][0]["dep_icao"], "KJFK")
        self.assertEqual(summary["top_routes"][0]["arr_icao"], "KLAX")
        self.assertEqual(summary["top_routes"][0]["flights"], 2)
        self.assertEqual(summary["recent_flights"][0]["callsign"], "UAL101")
        self.assertIn("United States", summary["countries"])


if __name__ == "__main__":
    unittest.main()
