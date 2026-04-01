import json
import data_manager as data_mng
from delivery_manager import create_delivery
import stats_manager as stats_mng
from delivery_input_validation import validate_input

def get_delivery_input():
    
    while True:

        distance = input("Distance parcourue (kilometres):")
        price    = input("Prix de la livraison :")
        duration = input("Durée de la livraison (minutes) :")

        try :
            distance = float(distance)
            price    = float(price)
            duration = float(duration)

            errors_list = validate_input(distance, price, duration)

            if errors_list:
                for error in errors_list:
                    print(f"\nErreur(s) détectée(s): {error}\n")
                
                continue
            
        except ValueError:
            print("Entrez une valeur numerique")
            continue
        
        return distance, price, duration


def main():
    
    actions = [
        "Ajouter une livraison",
        "Afficher mes livraisons",
        "Afficher mes statistiques",
        "Quitter",
    ]
    number_of_actions = len(actions)
    print("\nChoisissez parmis les options suivante :")

    while True:
        for i, action in enumerate(actions):
            print(f"{i + 1}. {action}")

        choice = input("\nQuel est votre choix ? ")
        
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
    
            print(f"\nSauvegarde de la livraison en date du {delivery['date']}\n")
                
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
