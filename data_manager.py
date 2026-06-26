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
            
            delivery_data = (
                             delivery_dict["delivery_distance"],
                             delivery_dict["delivery_price"],
                             delivery_dict["delivery_duration"],
                             delivery_dict["delivery_date"],
                             )
            with sqlite3.connect("deliveries.db")as connection:
                cursor = connection.cursor()
                cursor.execute("""
                                    INSERT INTO deliveries(distance, price, duration, date) 
                                    VALUES(?, ?, ?, ?)""", delivery_data
                                    )
                  

        except sqlite3.Error as e:
            return f"Erreur lors de l'enregistrement des données : {e}"
        
    def get_deliveries(self):
        delivery = self.cursor.execute("""SELECT id, distance, price, duration, date FROM deliveries""" )
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
    
    def delete_delivery(self, input_delivery_id):
        try:
            self.cursor.execute("DELETE FROM deliveries WHERE id = ?", (input_delivery_id,))
            self.connection.commit()

            if self.cursor.rowcount > 0:
                return True
            return False
        except sqlite3.Error:
            return False


    
    

        



