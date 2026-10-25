from app.repositories.database import DataBaseManager
from fastapi import  APIRouter, Depends
from app.schemas.schemas import StatsResponse
from app.dependencies import get_data_manager
data_manager = DataBaseManager()
router = APIRouter()

@router.get("/", status_code=200, response_model=StatsResponse)
async def get_stats(data_manager: DataBaseManager = Depends(get_data_manager)):
    return data_manager.get_stats()