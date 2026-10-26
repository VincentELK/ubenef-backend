import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.repositories.database import DataBaseManager 
from app.dependencies import get_data_manager


def get_test_data_manager():
    return DataBaseManager("tests/test.db")


@pytest.fixture
def test_context():
    app.dependency_overrides[get_data_manager] = get_test_data_manager
    testing_db = get_test_data_manager()
    testing_db.init_db()
    testing_db.delete_all_deliveries()
    client = TestClient(app)
    yield client
    app.dependency_overrides = {}