
def test_delete_deliveries(test_context):
    test_context.post("/deliveries", json={"distance": 5.0, "price": 3.0, "duration": 5.0})

    test_context.post("/deliveries", json={"distance": 8.0, "price": 3.0, "duration": 8.0})

    delete_response = test_context.delete("/deliveries")
    assert delete_response.status_code == 200
    response = test_context.get("/deliveries")
    response_json = response.json()
    assert isinstance(response_json, list)
    assert response.status_code == 200
    assert len(response_json) == 0

def test_delete_delivery_by_id(test_context):
    response = test_context.post("/deliveries", json={"distance": 5.0, "price": 3.0, "duration": 5.0})
    assert response.status_code == 200

    response_json = response.json()
    delivery_id = response_json["id"]
    delete_response = test_context.delete(f"/deliveries/{delivery_id}")
    assert delete_response.status_code == 200

    get_response = test_context.get(f"/deliveries/{delivery_id}")
    assert get_response.status_code == 404
    





    