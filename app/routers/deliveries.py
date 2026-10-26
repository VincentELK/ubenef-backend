from app.schemas.schemas import CreateDelivery, DeliveryResponse
from app.validators.validation import validate_input
from app.repositories.database import DataBaseManager
from fastapi import Depends, HTTPException, APIRouter
from app.models.delivery import Delivery
from app.dependencies import get_data_manager

router = APIRouter()

@router.get("/", status_code=200, response_model=list[DeliveryResponse])
async def get_deliveries(data_manager: DataBaseManager = Depends(get_data_manager)): 
    deliveries_obj_list = data_manager.get_deliveries()
    deliveries_dict_list = []
    for delivery in deliveries_obj_list:
        delivery_dict = delivery.to_dict()
        deliveries_dict_list.append(delivery_dict)
    return deliveries_dict_list

@router.get("/{id}", status_code=200, response_model=DeliveryResponse)
async def get_delivery_by_id(id: int, data_manager: DataBaseManager = Depends(get_data_manager)):
    delivery = data_manager.get_delivery_by_id(id)
    if not delivery:
        raise HTTPException(status_code=404, detail="ID not found")
    return delivery

    
@router.post("/", status_code=201, response_model=DeliveryResponse)
async def save_delivery(delivery_info: CreateDelivery, data_manager: DataBaseManager = Depends(get_data_manager)) :

    error_dict = validate_input(delivery_info.distance, delivery_info.price, delivery_info.duration)
    if not error_dict:
        delivery_obj = Delivery(delivery_info.distance, delivery_info.price, delivery_info.duration)
        data_manager.save_delivery(delivery_obj)
        return delivery_obj
    else:
        raise HTTPException(status_code=400, detail=error_dict)
        
    
@router.delete("/{delivery_id}", status_code=200)
async def delete_delivery(delivery_id: int, data_manager: DataBaseManager = Depends(get_data_manager)):
    if not data_manager.delete_delivery(delivery_id):
        raise HTTPException(status_code=404, detail="This ID doesn't exist")
    return {"message": f"Delivery number {delivery_id} has been deleted"}

@router.delete("/", status_code=200)
async def delete_all_deliveries(data_manager: DataBaseManager = Depends(get_data_manager)):
    if not data_manager.delete_all_deliveries():
        raise HTTPException(status_code=404, detail="There is no delivery saved")
    else:
        return {"Message": f"Every delivery has been deleted sucessfully"}
    