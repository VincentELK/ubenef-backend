from app.repositories.database import DataBaseManager
from fastapi import FastAPI, HTTPException, APIRouter
from app.schemas.schemas import StatsResponse

data_manager = DataBaseManager()
router = APIRouter()

@router.get("/", status_code=200, response_model=StatsResponse)
async def get_stats():
    return data_manager.get_stats()