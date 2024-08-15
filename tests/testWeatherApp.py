import unittest
from datetime import datetime
from fastapi import HTTPException

from Connectors.connector import DbConnection
from DomaIn.weatherMeasurement import WeatherMeasurement
from Services.weatherServices import WeatherServices

class TestWeatherServices(unittest.TestCase):

    def setUp(self):
        self.db = DbConnection()
        self.db.execute_query('''
            CREATE TABLE IF NOT EXISTS weather_measurements (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                station_id INTEGER NOT NULL,
                date_time TEXT NOT NULL,
                temperature REAL NOT NULL,
                humidity REAL NOT NULL,
                wind_speed REAL NOT NULL,
                wind_direction TEXT NOT NULL,
                rainfall REAL NOT NULL
            )
        ''')

    def test_create_measurement_valid_data(self):
        service = WeatherServices()
        measurement = WeatherMeasurement(
            station_id=50,
            date_time=datetime.now().isoformat(),
            temperature=25,
            humidity=50,
            wind_speed=15,
            wind_direction="N",
            rainfall=5.0
        )
        response = service.create_measurement(measurement)
        self.assertEqual(response["message"], "Η μέτρηση καταχωρήθηκε επιτυχώς")

    def test_create_measurement_invalid_temperature(self):
        service = WeatherServices()
        measurement = WeatherMeasurement(
            station_id=1,
            date_time=datetime.now().isoformat(),
            temperature=-100,
            humidity=50,
            wind_speed=15,
            wind_direction="N",
            rainfall=5.0
        )
        with self.assertRaises(HTTPException) as context:
            service.create_measurement(measurement)
        self.assertEqual(context.exception.status_code, 400)

if __name__ == "__main__":
    unittest.main()
