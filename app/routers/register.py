from app.repositories.database import DataBaseManager
from fastapi import  APIRouter, Depends, HTTPException
from app.dependencies import get_data_manager
from app.schemas.schemas import UserIn, CreateUserResponse
from app.security import get_password_hash, verify_hash
data_manager = DataBaseManager()
router = APIRouter()

@router.post("/", status_code=200, response_model=CreateUserResponse)
async def user_register(user_info : UserIn, data_manager : DataBaseManager = Depends(get_data_manager)):
    
    pwd_hash = get_password_hash(user_info.password)
    
    user_dict_infos = data_manager.create_user(user_info.username, pwd_hash, user_info.email, user_info.disabled)    
    if  not user_dict_infos:
        raise HTTPException(status_code=400, detail="Nom d'utilisateur ou email déjà utilisé")
    return user_dict_infos 