from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app
from app.repositories.database import DataBaseManager 
from app.dependencies import get_data_manager


def get_test_data_manager():
    return DataBaseManager("tests/test.db")

app.dependency_overrides[get_data_manager] = get_test_data_manager

testing_db = get_test_data_manager()

testing_db.init_db()
testing_db.delete_deliveries()
client = TestClient(app)

def test_get_deliveries_empty():

    response = client.get("/deliveries")
    
    assert response.status_code == 200
    assert response.json() == []

def test_get_deliveries():
    client.post("/deliveries", json={"distance": 5.0, "price": 3.0, "duration": 5.0})
    response = client.get("/deliveries")
    response_json = response.json()
    assert response.status_code == 200
    assert isinstance(response_json, list)
    assert len(response_json) >= 1

