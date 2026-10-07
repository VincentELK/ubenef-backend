from app.repositories.database import DataBaseManager
from fastapi import FastAPI
from app.models.delivery import Delivery
import app.cli.menus as menus
from pydantic import BaseModel
from app.validators.validation import validate_input
data_manager = DataBaseManager()

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/deliveries")
async def get_deliveries():
    deliveries_obj_list = data_manager.get_deliveries()
    delivery_dict_list = []
    for delivery in deliveries_obj_list:
        delivery_dict = delivery.to_dict()
        delivery_dict_list.append(delivery_dict)
    return delivery_dict_list

class Delivery_info(BaseModel):
    distance: float
    price: float
    duration: float

@app.post("/delivery")
async def send_delivery(delivery_info: Delivery_info ):

    error_dict = validate_input(delivery_info.distance, delivery_info.price, delivery_info.duration)
    if not error_dict:
        delivery_obj = Delivery(delivery_info.distance, delivery_info.price, delivery_info.duration)
        data_manager.save_delivery(delivery_obj)
        return delivery_info
    else:
        return error_dict
    
@app.delete("/delivery/{delivery_id}")
async def delete_delivery(delivery_id: int):
    data_manager.delete_delivery(delivery_id)
    return {"Message": f"Delivery number {delivery_id} as been deleted"}

def main():
    data_manager.init_db()
    print("Db initialisée")
    menus.member_main_menu()
    
    

        



    
    
   

             
             
                
       


    
if __name__ == "__main__":
    main()
