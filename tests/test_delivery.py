from datetime import datetime

from app.models.delivery import Delivery


def test_delivery_to_dict():
    test_delivery = Delivery(5.0, 3.0, 5.0, "10/05/2026", 2)

    assert test_delivery.to_dict() == {"id": 2, "distance": 5.0, "price": 3.0, "duration": 5.0, "date": "10/05/2026"}


def test_get_date():
    
    time_date = datetime.now()
    actual_date = time_date.date()
    formated_date = "%s/%s/%s" %(actual_date.day, actual_date.month, actual_date.year)
    test_delivery = Delivery(5.0, 3.0, 5.0)

    assert test_delivery.date == formated_date
