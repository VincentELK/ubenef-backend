import json
import data_manager as data_mng
from delivery_manager import create_delivery
import stats_manager as stats_mng


def get_delivery_input():
    while True:

        distance = input("Distance parcourue :")
        price    = input("Prix de la livraison :")
        duration = input("Durée de la livraison :")
        try :
            distance = float(distance)
            price    = float(price)
            duration = float(duration)
        except ValueError:
            print("Entrez une valeur numerique")
            continue
        break
    return distance,price,duration


def main():
    
    actions = [
        "Ajouter une livraison",
        "Afficher mes livraisons",
        "Afficher mes statistiques",
        "Quitter",
    ]
    number_of_actions = len(actions)
    print("Choisissez parmis les options suivante :")

    while True:
        for i, action in enumerate(actions):
            print(f"{i + 1}. {action}")

        choice = input("Quel est votre choix ? ")
        
        try: 
            choice = int(choice)
        except ValueError:
            
            print(f"veuillez choisir un choix valide entre 1 et {number_of_actions}")
            continue

        if not choice in range(1, number_of_actions + 1):
            print(f"veuillez choisir un choix valide entre 1 et {number_of_actions}")
            continue


        if choice == 1:
            distance,price,duration = get_delivery_input()

            delivery = create_delivery(distance, price, duration)
            data_mng.save_data(delivery)
    
            print(f"Sauvegarde de la livraison en date du {delivery['date']}")
                

        elif choice == 2:
            print("Affichage des livraisons sauvegardées :")

            data_mng.display_delivery_list()

        elif choice == 3:
            delivery_list = data_mng.load_data()
            total_distance = stats_mng.total_distance(delivery_list)
            print("-" * 10)
            print("Affichage des statistiques :\n")
            print(f"Distance totale : {total_distance} KM")
            print("-" * 10)
            
            
        elif choice == len(actions):
            print("Fermeture de Ubenef, à bientot !")
            break
        



    
    
   

             
             
                
       


    
if __name__ == "__main__":
    main()
