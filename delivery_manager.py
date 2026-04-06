
from datetime import datetime

class Delivery():
    def __init__(self, distance, price, duration, date=None):
        self.distance = distance
        self.price = price
        self.duration = duration
        self.date = date if date else self.get_date()

    def get_date(self):
        time_data = datetime.now()
        date = time_data.date()
        formated_date = "%s/%s/%s" %(date.day, date.month, date.year)
        return formated_date
    
    def to_dict(self):
        return {"delivery_distance": self.distance, "delivery_price": self.price, "delivery_duration": self.duration, "delivery_date": self.date}

    def price_per_kilometer(self):
        return round(self.price / self.distance, 2)



