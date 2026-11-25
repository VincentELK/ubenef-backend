from app.repositories.database import DataBaseManager
from fastapi import  APIRouter, Depends, HTTPException, status
from datetime import  timedelta
from app.config import ACCESS_TOKEN_EXPIRE_MINUTES
from app.dependencies import get_data_manager
from app.schemas.schemas import UserIn, UserOut 
from app.security import get_password_hash, authenticate_user, create_access_token
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.schemas.schemas import TokenData, Token
data_manager = DataBaseManager()
router = APIRouter()

@router.post("/register", status_code=201, response_model=UserOut)
async def user_register(
    user_info: UserIn,
    data_manager: DataBaseManager = Depends(get_data_manager)
):
    pwd_hash = get_password_hash(user_info.password)
    
    user_dict_infos = data_manager.create_user(
        user_info.username,
        pwd_hash,
        user_info.email,
        False  
    )

    if not user_dict_infos:
        raise HTTPException(
            status_code=400,
            detail="Nom d'utilisateur ou email déjà utilisé"
        )

    return user_dict_infos

@router.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],) -> Token:
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    access_token = create_access_token(data={"sub": user["username"]}, expires_delta=access_token_expires)

    return Token(access_token=access_token, token_type="bearer")            



