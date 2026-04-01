def validate_input(distance, price, duration):
    error_list = []
    distance_boundary = (1, 30)
    price_boundary = (1, 20)
    duration_boundary = (1, 40)

    

    
    
    if not distance_boundary[0] <= distance <= distance_boundary[1]:
        distance_error_msg = f"Input distance {distance} out of boundary {distance_boundary[0]} - {distance_boundary[1]}"

        error_list.append(distance_error_msg)

    if not price_boundary[0] <= price <= price_boundary[1]:
        price_error_msg = f"Input price {price} out of boundary {price_boundary[0]} - {price_boundary[1]} "

        error_list.append(price_error_msg)
    
    if not duration_boundary[0] <= duration <= duration_boundary[1]:
        
        duration_error_msg = f"Input duration {duration} out of boudary {duration_boundary[0]} - {duration_boundary[1]}"

        error_list.append(duration_error_msg)
    
    return error_list




