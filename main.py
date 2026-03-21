import json


def main():
    connect = True
    saved = False
    while connect:
        distance = input("Distance : ")
        price = input("Price : ")
        
        

        while not saved:
            save_input = input(f"Do you want to save data? :\n distance : {distance}\n price : {price}\n (y/n)")
            lower_input = save_input.lower()
            
            if lower_input != "y" and lower_input != "n":
                print("Wrong key, use Y or N to make a choice")
                continue
            elif lower_input == "y":
                course = {"distance": int(distance), "price": float(price)}
                saved = True
                connect = False
            else:
                break
        connect = False
                
       


    
if __name__ == "__main__":
    main()
