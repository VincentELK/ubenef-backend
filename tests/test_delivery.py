import pytest
from delivery_manager import Delivery
from datetime import datetime
def test_delivery_to_dict():
    test_delivery = Delivery(5.0, 3.0, 5.0, "10/05/2026", 2)

    assert test_delivery.to_dict() == {"delivery_id": 2, "delivery_distance": 5.0, "delivery_price": 3.0, "delivery_duration": 5.0, "delivery_date": "10/05/2026"}

def test_price_per_kilometer():
    test_delivery = Delivery(5.0, 3.0, 5.0, "10/05/2026", 2)
    assert test_delivery.price_per_kilometer() == 0.6

def test_get_date():
    
    time_date = datetime.now()
    actual_date = time_date.date()
    formated_date = "%s/%s/%s" %(actual_date.day, actual_date.month, actual_date.year)
    test_delivery = Delivery(5.0, 3.0, 5.0)

    assert test_delivery.date == formated_date
