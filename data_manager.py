import json
from json import JSONDecodeError


def load_data():
    try:
        with open("courses.json", "r") as f:
            data = json.load(f)
            if not data :
                data = []
        return data
    except FileNotFoundError:
        data = []
        return data
    except JSONDecodeError:
        data = []
        return data
    
def save_data(delivery_data):
    
    try :
        data = load_data()
        
        if not data:
            print(f"Premiere sauvegarde")

        
        
        data.append(delivery_data)
        with open("courses.json", "w") as f:
            json.dump(data, f, indent=2)
                
        
    except FileNotFoundError:
        print("Fichier introuvable")

def display_delivery_list():
    data = load_data()

    for delivery in data:
        delivery_distance = delivery["distance"]
        delivery_price    = delivery["price"]
        delivery_duration = delivery["duration"]
        delivery_date     = delivery["date"]
        print(f"""\n-------------------------------\n 
              Livraison du {delivery_date}:\n
              Montant : {delivery_price} EU\n
              Distance : {delivery_distance} KM\n
              Durée : {delivery_duration} minutes\n
-------------------------------------
""")
    
    

        



