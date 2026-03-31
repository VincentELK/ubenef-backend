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

def average_turnover(delivery_list):
    return total_turnover(delivery_list) / len(delivery_list)

def price_by_kilometer(distance, turnover):

    return round(turnover/distance,2)

def total_duration(delivery_list):
    total = 0
    for delivery in delivery_list:
        total_duration +=  delivery["duration"]
    return total

def price_by_hour(price, duration):
    hour = duration / 60
    return round(price / hour,2)