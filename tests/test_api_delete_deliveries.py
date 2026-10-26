
from fastapi.testclient import TestClient
from app.main import app
from app.repositories.database import DataBaseManager 
from app.dependencies import get_data_manager
client = TestClient(app)

def get_test_data_manager() -> DataBaseManager:
    return DataBaseManager("tests/test.db")

app.dependency_overrides[get_data_manager] = get_test_data_manager


def test_delete_deliveries():
    client.post("/deliveries", json={"distance": 5.0, "price": 3.0, "duration": 5.0})

    client.post("/deliveries", json={"distance": 8.0, "price": 3.0, "duration": 8.0})

    delete_response = client.delete("/deliveries")
    assert delete_response.status_code == 200
    response = client.get("/deliveries")
    response_json = response.json()
    assert isinstance(response_json, list)
    assert response.status_code == 200
    assert len(response_json) == 0