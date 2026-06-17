import json
from data_manager import DataBaseManager
from delivery_manager import Delivery
import stats_manager as stats_mng
from delivery_input_validation import validate_input
data_manager = DataBaseManager()

def get_delivery_input():
    
    while True:

        distance = input("Distance parcourue (kilometres): ")
        price    = input("Prix de la livraison: ")
        duration = input("Durée de la livraison (minutes): ")

        try :
            distance = float(distance)
            price    = float(price)
            duration = float(duration)

            errors_list = validate_input(distance, price, duration)

            if errors_list:
                print(f"\nErreur(s) détectée(s):\n")
                for error in errors_list:
                    print(f"{error}\n")
                
                continue

            delivery = Delivery(distance, price, duration)
        except ValueError:
            print("Entrez une valeur numerique")
            continue
        
        return delivery


def main():
    
    actions = [
        "Ajouter une livraison",
        "Afficher mes livraisons",
        "Supprimer une livraison",
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
            new_delivery = get_delivery_input()
            
            data_manager.save_delivery(new_delivery)
            
    
            print(f"\nSauvegarde de la livraison en date du {new_delivery.date}\n")
                
        elif choice == 2:
            if data_manager.get_deliveries():
                print("\n-----Affichage des livraisons sauvegardées :-----\n")

                for delivery in data_manager.get_deliveries():
                    
                    print(f"Livraison du {delivery.date}")
                    print(f"  - ID       : {delivery.id}")
                    print(f"  - Distance : {delivery.distance} km")
                    print(f"  - Temps    : {delivery.duration} min")
                    print(f"  - Prix     : {delivery.price} Euros\n")
            else:
                print("\nAucunes livraisons enregistrée\n")
            

        elif choice == 3:
            while True:
                
                if not data_manager.get_deliveries():
                    print("\n----Il n'y a aucunes livraisons enregistrée----\n")
                    break
                try:
                    delivery_id_to_delete = int(input("Selectionner l'id de la course a suprimer: \n"))

                except ValueError:
                    print("!! Saisie invalide !!")

                    break
                if data_manager.delete_delivery(delivery_id_to_delete):
                    print(f"\nLa livraison {delivery_id_to_delete} à bien été supprimer!\n")
                else:
                    print(f"\nL'ID {delivery_id_to_delete} n'existe pas\n")
                break

            

          
            
            
        elif choice == len(actions):
            print("\nFermeture de Ubenef, à bientot !")
            break
        



    
    
   

             
             
                
       


    
if __name__ == "__main__":
    main()
