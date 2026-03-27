import json
from datetime import datetime


def create_delivery(distance, price, duration):
    
    time_data = datetime.now()
    date = time_data.date()
    formated_date = "%s/%s/%s" %(date.day, date.month, date.year)

    
    delivery_data = {"date":formated_date, 
                     "distance":distance, 
                     "price": price, 
                     "duration": duration
                     }
    
    return delivery_data

