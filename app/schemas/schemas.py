from pydantic import BaseModel

class CreateDelivery(BaseModel):
    distance: float
    price: float
    duration: float

class DeliveryResponse(BaseModel):
    id: int
    distance: float
    price: float
    duration: float
    date: str

class StatsResponse(BaseModel):
    total_deliveries: int
    total_price: float
    total_duration: float
    total_distance: float
    average_distance: float
    average_price: float
    average_duration: float