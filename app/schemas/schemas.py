from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    disabled: bool

class CreateUserResponse(BaseModel):
    username: str
    email: str

class UserIn(UserBase):
    password: str
    
class UserOut(UserBase):
    pass 

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