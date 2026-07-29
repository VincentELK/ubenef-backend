import json
from json import JSONDecodeError
from delivery_manager import Delivery
import sqlite3
import logging

logging.basicConfig(filename='data_manager.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DataBaseManager():
    def __init__(self) -> None:
        self.db_path = "deliveries.db"


    def init_db(self):
        try:
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()

                cursor.execute("""
                                    CREATE TABLE IF NOT EXISTS deliveries(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    distance REAL NOT NULL,
                                    price REAL NOT NULL,
                                    duration REAL NOT NULL,
                                    date TEXT NOT NULL
                                    );""")
                
                cursor.execute(""" CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    username TEXT NOT NULL UNIQUE,
                                    password_hash TEXT NOT NULL,
                                    email TEXT NOT NULL UNIQUE);""")
        except sqlite3.Error as e:
            logging.error(f"Erreur lors de la creation de tables : {e}")



    def save_delivery(self, delivery_obj):
        try:
            delivery_dict = delivery_obj.to_dict()
            
            delivery_data = (
                             delivery_dict["delivery_distance"],
                             delivery_dict["delivery_price"],
                             delivery_dict["delivery_duration"],
                             delivery_dict["delivery_date"],
                             )
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()
                cursor.execute("""
                                    INSERT INTO deliveries(distance, price, duration, date) 
                                    VALUES(?, ?, ?, ?)""", delivery_data
                                    )
                  

        except sqlite3.Error as e:
            logging.error(f"Erreur lors de l'enregistrement des données : {e}")

        
    def get_deliveries(self):

        try :
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()

                delivery = cursor.execute("""SELECT id, distance, price, duration, date FROM deliveries""" )
                deliveries_object_list = []
                for row in delivery:
                    db_id = row[0]
                    db_distance = row[1]
                    db_price = row[2]
                    db_duration = row[3]
                    db_date = row[4]
                    delivery_object = Delivery(db_distance, db_price, db_duration, db_date, db_id)
                    deliveries_object_list.append(delivery_object)
                return deliveries_object_list
        except sqlite3.Error as e:
            logging.error(f"Erreur lors de la récupération des données : {e}")
            return []
    
    def delete_delivery(self, input_delivery_id):
        try:
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM deliveries WHERE id = ?", (input_delivery_id,))
                
                if cursor.rowcount > 0:
                    return True
                return False
        except sqlite3.Error as e:
            logging.error(f"Erreur lors de la suppression de livraison : {e}")
            return False


    
    

        



