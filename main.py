import json
import data_manager as data_mng
from delivery_manager import create_delivery

def main():
    valid_inputs = ["y", "n"]
    
    while True:
        distance = input("Distance : ")
        price = input("Price : ")
        duration = input("duration (minutes) : ")

        try:
            distance = int(distance)
            price    = float(price)
            duration = int(duration)
        except ValueError:
            print("input must be number")
            continue
        
        while True:
            
            save_input = input(f"Do you want to save data? :\n distance : {distance}\n price : {price}\n duration : {duration}  (y/n)\n")

            lower_input = save_input.lower()
                
            if lower_input not in valid_inputs:
                    print("Wrong key, use Y or N to make a choice")
                    continue

            elif lower_input == "y":
                    delivery = create_delivery(distance, price, duration)
                    data_mng.save_data(delivery)
                    break
                    
            else:

                break

        add_more_delivery_input = input("Do you want to add one more delivery ? (y/n)\n" )
        while not add_more_delivery_input.lower() in valid_inputs:
             print("Use a valid key Y/N")
             add_more_delivery_input = input("Do you want to add one more delivery ? (y/n)\n" )
             continue
        if  add_more_delivery_input.lower() == "y":
             print("Add a new delivery")
             continue
        
        display_delivery_input = input("Do you want to display your delivery list? (y/n)")

        while not display_delivery_input.lower() in valid_inputs:
             print("Use a valid key Y/N")
             display_delivery_input = input("Do you want to display your delivery list? (y/n)")
             

        if display_delivery_input == "y":
             data_mng.display_delivery_list()
             break
        else:
             break
             
             
             
                
       


    
if __name__ == "__main__":
    main()
