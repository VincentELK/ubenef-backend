import json
import data_manager as data_mng
from delivery_manager import create_delivery
import stats_manager as stats_mng


def get_delivery_input():
    distance_boundary = (1, 30)
    price_boundary = (1, 20)
    duration_boundary = (1, 40)
    while True:

        distance = input("Distance parcourue (kilometres):")
        price    = input("Prix de la livraison :")
        duration = input("Durée de la livraison (minutes) :")
        try :
            distance = float(distance)
            price    = float(price)
            duration = float(duration)

            if not distance_boundary[0] <= distance <= distance_boundary[1]:
                print(f"La valeur de distance : {distance}, doit etre comprise entre {distance_boundary[0]} et {distance_boundary[1]}")
                continue
            if not price_boundary[0] <=  price <= price_boundary[1]:
                print(f"La valeur de prix : {price}, doit etre comprise entre {price_boundary[0]} et {price_boundary[1]}")
                continue
            if not duration_boundary[0] <= duration <= duration_boundary[1]:
                print(f"La valeur de temp {duration} doit etre comprise entre {duration_boundary[0]} et {duration_boundary[1]}")
                continue

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
    
            print(f"\nSauvegarde de la livraison en date du {delivery['date']}\n1")
                
        elif choice == 2:
            print("Affichage des livraisons sauvegardées :")

            data_mng.display_delivery_list()

        elif choice == 3:
            
            delivery_list = data_mng.load_data()
            if not delivery_list:
                print("------\nAucune statistiques à afficher...\n-----")
                continue
            
            total_distance = stats_mng.total_distance(delivery_list)
            average_turnover = stats_mng.average_turnover(delivery_list)
            total_turnover = stats_mng.total_turnover(delivery_list)
            total_duration = stats_mng.total_duration(delivery_list)
            price_by_distance = stats_mng.price_by_kilometer(total_distance, total_turnover)
            print("------- Mes statistiques ------ :\n")
            print(f"Nombre de livraisons total : {len(delivery_list)}")
            print(f"Distance totale : {total_distance} KM")
            print(f"Chiffre d'affaire total : {total_turnover} euros")
            print(f"Moyenne de chiffre d'affaire : {average_turnover} euros ")
            print(f"Revenue au Kilomètre : {price_by_distance}")
            print(f"Temp de livraison total (minutes) : {total_duration}")
            print(f"Revenue de l'heure : {stats_mng.price_by_hour(total_turnover, total_duration)}")
            print("=" * 40)

            
            
        elif choice == len(actions):
            print("\nFermeture de Ubenef, à bientot !")
            break
        



    
    
   

             
             
                
       


    
if __name__ == "__main__":
    main()
