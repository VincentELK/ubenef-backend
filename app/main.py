from app.repositories.database import DataBaseManager
import app.cli.menus as menus
from fastapi import FastAPI
from app.routers import deliveries, stats
data_manager = DataBaseManager()
data_manager.init_db()
print("Db initialisée")

app = FastAPI()
app.include_router(deliveries.router, prefix="/deliveries", tags=["deliveries"])
app.include_router(stats.router, prefix="/stats", tags=["stats"])
