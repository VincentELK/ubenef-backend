import json
from json import JSONDecodeError
from delivery_manager import Delivery

class DataManager():
    def __init__(self):
        self.filepath = "courses.json"

    def load_deliveries(self):
        try:
            with open(self.filepath, "r") as f:
                deliverys_list = json.load(f)
                if not deliverys_list:
                    deliverys_list = []
                deliveries_object_list = []
                
                for delivery in deliverys_list:
                    delivery_date = delivery["delivery_date"]
                    distance = delivery["delivery_distance"]
                    price    = delivery["delivery_price"]
                    duration = delivery["delivery_duration"]

                    delivery_object = Delivery(distance, price, duration, delivery_date)
                    deliveries_object_list.append(delivery_object)

                return deliveries_object_list
                       
        except (FileNotFoundError, JSONDecodeError):
            deliverys_list = []
            return deliverys_list
    
    def save_delivery(self, delivery_obj):
        try:
            deliveries_list_obj = self.load_deliveries()
            
            deliveries_list_obj.append(delivery_obj)
            deliveries_data_list = [data.to_dict() for data in deliveries_list_obj] # get all data from the deliveries_list_obj -> dict -> list

            with open(self.filepath, "w") as f:
                json.dump(deliveries_data_list, f, indent=2)

        except FileNotFoundError:
            return f"No file found at {self.filepath}"



    
    

        



