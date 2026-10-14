from app.repositories.database import DataBaseManager
from fastapi import FastAPI, HTTPException
from app.models.delivery import Delivery
import app.cli.menus as menus
from pydantic import BaseModel
from app.schemas.schemas import CreateDelivery, DeliveryResponse
from app.validators.validation import validate_input
data_manager = DataBaseManager()

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/deliveries", status_code=200, response_model=list[DeliveryResponse])
async def get_deliveries(): 
    deliveries_obj_list = data_manager.get_deliveries()
    deliveries_dict_list = []
    for delivery in deliveries_obj_list:
        delivery_dict = delivery.to_dict()
        deliveries_dict_list.append(delivery_dict)
    return deliveries_dict_list


@app.post("/deliveries", status_code=201, response_model=DeliveryResponse)
async def save_delivery(delivery_info: CreateDelivery) :

    error_dict = validate_input(delivery_info.distance, delivery_info.price, delivery_info.duration)
    if not error_dict:
        delivery_obj = Delivery(delivery_info.distance, delivery_info.price, delivery_info.duration)
        data_manager.save_delivery(delivery_obj)
        return delivery_obj
    else:
        raise HTTPException(status_code=400, detail=error_dict)
        
    
@app.delete("/deliveries/{delivery_id}", status_code=200)
async def delete_delivery(delivery_id: int):
    if not data_manager.delete_delivery(delivery_id):
        raise HTTPException(status_code=404, detail="This ID doesn't exist")
    return {"message": f"Delivery number {delivery_id} has been deleted"}
    

def main():
    data_manager.init_db()
    print("Db initialisée")
    menus.member_main_menu()
    
    

        



    
    
   

             
             
                
       


    
if __name__ == "__main__":
    main()
