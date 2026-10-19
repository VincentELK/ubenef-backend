from app.repositories.database import DataBaseManager
import app.cli.menus as menus
from fastapi import FastAPI
from app.routers import deliveries, stats
data_manager = DataBaseManager()
app = FastAPI()

app.include_router(deliveries.router, prefix="/deliveries", tags=["deliveries"])
app.include_router(stats.router, prefix="/stats", tags=["stats"])
def main():
    data_manager.init_db()
    print("Db initialisée")
    menus.member_main_menu()

if __name__ == "__main__":
    main()
