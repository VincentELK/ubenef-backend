
from datetime import datetime
class Delivery:
    def __init__(self, distance, price, duration, date=None, id=None):
        self.id = id
        self.distance = distance
        self.price = price
        self.duration = duration
        self.date = date if date else self.get_date()

    def get_date(self):
        time_data = datetime.now()
        date = time_data.date()
        formated_date = "%s/%s/%s" %(date.day, date.month, date.year)
        return formated_date
    
    def to_dict(self) -> dict:
        return {
        "id": self.id,
        "distance": self.distance, 
        "price": self.price,
        "duration": self.duration, 
        "date": self.date
        }





