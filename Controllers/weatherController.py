from fastapi import APIRouter, Depends
from pydantic import BaseModel
from Services.weatherServices import WeatherServices
from DomaIn.weatherMeasurement import WeatherMeasurement
from Services.auth import get_current_user

router = APIRouter()


class MeasurementCreateUpdate(BaseModel):
    station_id: int
    date_time: str
    temperature: float
    humidity: float
    wind_speed: float
    wind_direction: str
    rainfall: float


@router.post('/create')
async def create_measurement(measurement: MeasurementCreateUpdate):
    service = WeatherServices()
    new_measurement = WeatherMeasurement(**measurement.dict())
    return service.create_measurement(new_measurement)


@router.get('/measurements', dependencies=[Depends(get_current_user)])
async def get_measurements(station_id: int = None, start_date: str = None, end_date: str = None):
    service = WeatherServices()
    return service.get_measurements(station_id, start_date, end_date)


@router.put('/update')
async def update_measurement(measurement: MeasurementCreateUpdate):
    service = WeatherServices()
    updated_measurement = WeatherMeasurement(**measurement.dict())
    return service.update_measurement(updated_measurement)
