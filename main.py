from app.repositories.database import DataBaseManager
from fastapi import FastAPI
import app.cli.menus as menus
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


def main():
    
    data_manager.init_db()
    print("Db initialisée")
    menus.member_main_menu()
    
    

        



    
    
   

             
             
                
       


    
if __name__ == "__main__":
    main()
