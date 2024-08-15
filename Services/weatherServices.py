from DomaIn.weatherMeasurement import WeatherMeasurement
from Connectors.repoWeatherData import RepositoryWeather
from fastapi import HTTPException

class WeatherServices:
    repo = RepositoryWeather()

    def create_measurement(self, measurement: WeatherMeasurement):
        if not (-50 <= measurement.temperature <= 60):
            raise HTTPException(status_code=400, detail="Temperature out of range")
        if not (0 <= measurement.humidity <= 100):
            raise HTTPException(status_code=400, detail="Humidity out of range")
        if not (0 <= measurement.wind_speed <= 200):
            raise HTTPException(status_code=400, detail="Wind speed out of range")

        self.repo.insert_measurement(measurement)
        return {"message": "Η μέτρηση καταχωρήθηκε επιτυχώς"}

    def get_measurements(self, station_id=None, start_date=None, end_date=None):
        return self.repo.get_measurements(station_id, start_date, end_date)

    def update_measurement(self, measurement: WeatherMeasurement):
        self.repo.update_measurement(measurement)
        return {"message": "Η μέτρηση ενημερώθηκε επιτυχώς"}
