import json
from datetime import datetime
time_data = datetime.now()

def create_delivery(distance, price, duration):
    date = time_data.date()
    formated_date = "%s/%s/%s" %(date.day, date.month, date.year)

    
    delivery_data = {"date":formated_date, 
                     "distance":distance, 
                     "price": price, 
                     "duration": duration
                     }
    
    return delivery_data

