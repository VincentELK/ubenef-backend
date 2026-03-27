import json


def total_distance(delivery_list):
    total = 0
    for delivery in delivery_list:
        total += delivery["distance"]
    return total

def total_turnover(delivery_list):
    total_turnover = 0
    for delivery in delivery_list:
        total_turnover += delivery["price"]
    return total_turnover
