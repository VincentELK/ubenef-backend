
from app.repositories.database import DataBaseManager

data_manager = DataBaseManager()
import app.cli.menus as menus


def main():
    data_manager.init_db()
    print("Db initialisée")
    menus.member_main_menu()
    
    

        



    
    
   

             
             
                
       


    
if __name__ == "__main__":
    main()
