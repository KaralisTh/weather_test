class WeatherMeasurement:
    def __init__(self, station_id: int, date_time: str, temperature: float, humidity: float, wind_speed: float, wind_direction: str, rainfall: float):
        self.station_id = station_id
        self.date_time = date_time
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction
        self.rainfall = rainfall
