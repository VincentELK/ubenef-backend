import json
from json import JSONDecodeError
from delivery_manager import Delivery
import sqlite3



class DataBaseManager():
    def __init__(self):
        self.connection = sqlite3.connect("deliveries.db")
        self.cursor = self.connection.cursor()
        self.filepath = "courses.json"
    
    def create_deliveries_table(self):
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS deliveries(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            distance REAL NOT NULL,
                            price REAL NOT NULL,
                            duration REAL NOT NULL,
                            date TEXT NOT NULL
                            );""")
        self.connection.commit()


    def save_delivery(self, delivery_obj):
        try:
            delivery_dict = delivery_obj.to_dict()
            delivery_data = (delivery_dict["delivery_distance"],
                             delivery_dict["delivery_price"],
                             delivery_dict["delivery_duration"],
                             delivery_dict["delivery_date"],
                             )
            self.cursor.execute("""
                                INSERT INTO deliveries(distance, price, duration, date) 
                                VALUES(?, ?, ?, ?)""", delivery_data
                                )
            self.connection.commit()       

        except sqlite3.Error as e:
            return f"Erreur lors de l'enregistrement des données : {e}"
        
    def get_deliveries(self):
        delivery = self.cursor.execute("""SELECT distance, price, duration, date FROM deliveries""" )
        deliveries_object_list = []
        for row in delivery:
            

            db_distance = row[0]
            db_price = row[1]
            db_duration = row[2]
            db_date = row[3]
            delivery_object = Delivery(db_distance, db_price, db_duration, db_date)
            deliveries_object_list.append(delivery_object)
        return deliveries_object_list
    



    
    

        



