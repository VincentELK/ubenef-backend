import json
from data_manager import DataBaseManager
from delivery_manager import Delivery
import stats_manager as stats_mng
from delivery_input_validation import validate_input


def get_delivery_input():
    
    while True:

        distance = input("Distance parcourue (kilometres): ")
        price    = input("Prix de la livraison4" \
        ": ")
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
            new_delivery = get_delivery_input()
            data_manager = DataBaseManager()
            data_manager.save_delivery(new_delivery)
            
    
            print(f"\nSauvegarde de la livraison en date du {new_delivery.date}\n")
                
        elif choice == 2:
            print("Affichage des livraisons sauvegardées :")

            

        elif choice == 3:
            print("Modificatiosn en cours ...")
          
            
            
        elif choice == len(actions):
            print("\nFermeture de Ubenef, à bientot !")
            break
        



    
    
   

             
             
                
       


    
if __name__ == "__main__":
    main()
