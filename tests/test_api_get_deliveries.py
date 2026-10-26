
def test_get_deliveries_empty(test_context): # test_context from conftest file
    response = test_context.get("/deliveries")
    assert response.status_code == 200
    assert response.json() == []
    

def test_get_deliveries(test_context):
    test_context.post("/deliveries", json={"distance": 5.0, "price": 3.0, "duration": 5.0})
    response = test_context.get("/deliveries")
    response_json = response.json()
    assert response.status_code == 200
    assert isinstance(response_json, list)
    assert len(response_json) >= 1
    

