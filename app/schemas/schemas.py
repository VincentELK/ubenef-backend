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