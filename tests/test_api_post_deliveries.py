
def test_save_deliveries(test_context):
    response = test_context.post("/deliveries", json={"distance": 5.0, "price": 3.0, "duration": 5.0})

    assert response.status_code == 200
    data_json = response.json()
    assert data_json["distance"] == 5.0
    assert data_json["price"] == 3.0
    assert data_json["duration"] == 5.0
    assert "id" in data_json
    assert "date" in data_json