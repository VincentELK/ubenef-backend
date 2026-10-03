from data_manager import DataBaseManager
from delivery_input_validation import get_delivery_input

data_manager = DataBaseManager()


def guess_menu():
    actions = [
        "Connexion",
        "Inscription",
        "Calculateur rapide",
        "Quitter"
    ]
    number_of_actions = len(actions)

    while True:
        for i, action in enumerate(actions):
            print(f"{i + 1}. {action}")

        choice = input("\nSelectionnez une option: ")
        try: 
            choice = int(choice)
        except ValueError:
            
            print(f"veuillez choisir un nombre valide entre 1 et {number_of_actions}")
            continue

        if choice not in range(1, number_of_actions + 1):
            print(f"veuillez choisir un choix valide entre 1 et {number_of_actions}")
            continue


def member_main_menu():
        while True:

            actions = [
                "Ajouter une livraison",
                "Afficher mes livraisons",
                "Supprimer une livraison",
                "Quitter",
            ]
            number_of_actions = len(actions)
            print("\nChoisissez parmis les options suivante :")

            for i, action in enumerate(actions):
                print(f"{i + 1}. {action}")

            choice = input("\nQuel est votre choix ? ")
            
            try: 
                choice = int(choice)
            except ValueError:
                
                print(f"veuillez choisir un choix valide entre 1 et {number_of_actions}")
                continue

            if choice not in range(1, number_of_actions + 1):
                print(f"veuillez choisir un choix valide entre 1 et {number_of_actions}")
                continue

            if choice == 1:
                new_delivery = get_delivery_input()
                
                data_manager.save_delivery(new_delivery)
                
        
                print(f"\nSauvegarde de la livraison en date du {new_delivery.date}\n")
                    
            elif choice == 2:
                deliveries_list = data_manager.get_deliveries()
                if deliveries_list:
                    print("\n-----Affichage des livraisons sauvegardées :-----\n")

                    for delivery in deliveries_list:
                        
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