def test_get_stats_empty(test_context):
    response = test_context.get("/stats")
    assert response.json() == {
        "total_deliveries": 0,
        "total_price": 0,
        "total_duration": 0,
        "total_distance": 0,
        "average_distance": 0,
        "average_price": 0,
        "average_duration": 0,
    }


def test_get_stat(test_context):
    test_context.post("/deliveries", json={"distance": 8.0, "price": 3.0, "duration": 8.0})
    test_context.post("/deliveries", json={"distance": 2.0, "price": 3.0, "duration": 2.0})

    stats_response = test_context.get("/stats")
    assert stats_response.status_code == 200
    stats_response_json = stats_response.json()

    assert stats_response_json ["total_distance"] == 10.0
    assert stats_response_json ["total_deliveries"] == 2
    assert stats_response_json ["total_price"] == 6.0
    assert stats_response_json ["total_duration"] == 10.0

