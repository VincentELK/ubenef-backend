from delivery_manager import Delivery


def validate_input(distance, price, duration):
    errors_dict = {}
    distance_boundary = (0, 30)
    price_boundary = (0, 20)
    duration_boundary = (0, 40)

    
    if not distance_boundary[0] < distance <= distance_boundary[1]:
        distance_error_msg = f"Input distance {distance} out of boundary {distance_boundary[0]} - {distance_boundary[1]}"

        errors_dict["distance"] = {"error_message": distance_error_msg, "value": distance}

        

    if not price_boundary[0] < price <= price_boundary[1]:
        price_error_msg = f"Input price {price} out of boundary {price_boundary[0]} - {price_boundary[1]} "

        errors_dict["price"] = {"error_message": price_error_msg, "value": price}
        
    
    if not duration_boundary[0] < duration <= duration_boundary[1]:
        
        duration_error_msg = f"Input duration {duration} out of boudary {duration_boundary[0]} - {duration_boundary[1]}"

        errors_dict["duration"] = {"error_message": duration_error_msg, "value": duration}
    
    return errors_dict

def get_delivery_input():
    
    while True:

        distance = input("Distance parcourue (kilometres): ")
        price    = input("Prix de la livraison: ")
        duration = input("Durée de la livraison (minutes): ")

        try :
            distance = float(distance)
            price    = float(price)
            duration = float(duration)

            errors_dict = validate_input(distance, price, duration)

            if errors_dict:
                for error_data in errors_dict.values():
                    print(f'\n{error_data["error_message"]}\n')
                
                continue
                

            delivery = Delivery(distance, price, duration)
        except ValueError:
            print("Entrez une valeur numerique")
            continue
        
        return delivery




