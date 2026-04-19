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

        except FileNotFoundError:
            return f"No file found at {self.filepath}"

db_manager = DataBaseManager()
connection = db_manager.connection
db_manager.create_deliveries_table()
result = db_manager.cursor.execute("SELECT name FROM sqlite_master")
# query = "PRAGMA table_info(deliveries);"
# db_manager.cursor.execute(query)
# colonnes = db_manager.cursor.fetchall()

# for col in colonnes:
#     print(col)


    
    

        



