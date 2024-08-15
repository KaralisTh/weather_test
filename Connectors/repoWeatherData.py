from Connectors.connector import DbConnection
from DomaIn.weatherMeasurement import WeatherMeasurement

class RepositoryWeather:
    db = DbConnection()

    def insert_measurement(self, measurement: WeatherMeasurement):
        query = """
        INSERT INTO weather_measurements (station_id, date_time, temperature, humidity, wind_speed, wind_direction, rainfall)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        params = (
            measurement.station_id, measurement.date_time, measurement.temperature,
            measurement.humidity, measurement.wind_speed, measurement.wind_direction,
            measurement.rainfall
        )
        curr, conn = self.db.execute_query(query, params)
        conn.close()

    def get_measurements(self, station_id=None, start_date=None, end_date=None):
        query = "SELECT * FROM weather_measurements WHERE 1=1"
        params = []

        if station_id:
            query += " AND station_id = ?"
            params.append(station_id)
        if start_date and end_date:
            query += " AND date_time BETWEEN ? AND ?"
            params.extend([start_date, end_date])

        return self.db.fetch_data(query, tuple(params))

    def update_measurement(self, measurement: WeatherMeasurement):
        query = """
        UPDATE weather_measurements SET temperature = ?, humidity = ?, wind_speed = ?, wind_direction = ?, rainfall = ?
        WHERE station_id = ? AND date_time = ?
        """
        params = (
            measurement.temperature, measurement.humidity, measurement.wind_speed,
            measurement.wind_direction, measurement.rainfall,
            measurement.station_id, measurement.date_time
        )
        curr, conn = self.db.execute_query(query, params)
        conn.close()
