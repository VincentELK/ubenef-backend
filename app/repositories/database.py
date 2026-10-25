import logging
import sqlite3

from app.models.delivery import Delivery

logging.basicConfig(filename='data_manager.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DataBaseManager:
    def __init__(self, db_path="deliveries.db") -> None:
        self.db_path = db_path
        
    def init_db(self):
        try:
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()
                # creation de la table deliveries
                cursor.execute("""
                                    CREATE TABLE IF NOT EXISTS deliveries(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    distance REAL NOT NULL,
                                    price REAL NOT NULL,
                                    duration REAL NOT NULL,
                                    date TEXT NOT NULL
                                    );""")
                # creation de la table users
                cursor.execute(""" CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    username TEXT NOT NULL UNIQUE,
                                    password_hash TEXT NOT NULL,
                                    email TEXT NOT NULL UNIQUE);""")
        except sqlite3.Error as e:
            logging.error(f"Erreur lors de la creation de tables : {e}")

    def delete_deliveries(self):
        try: 
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM deliveries")
                if cursor.rowcount > 0:
                    return True
                return False
        except sqlite3.Error as e:
            logging.error(f"Erreur lors de la suppression des donnés : {e}")


    def save_delivery(self, delivery_obj):
        try:
            delivery_dict = delivery_obj.to_dict()
            
            delivery_data = (
                             delivery_dict["distance"],
                             delivery_dict["price"],
                             delivery_dict["duration"],
                             delivery_dict["date"],
                             )
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()
                cursor.execute("""
                                    INSERT INTO deliveries(distance, price, duration, date) 
                                    VALUES(?, ?, ?, ?)""", delivery_data
                                    )
                  
                delivery_obj.id = cursor.lastrowid  # recupere l'id du dernier INSERT
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
        
    def get_delivery_by_id(self, id):
        try:
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT id, distance, price, duration, date FROM deliveries WHERE id = ?", (id,))
                delivery = cursor.fetchone()
                if not delivery:
                    return None
                id = delivery[0]
                distance = delivery[1]
                price = delivery[2]
                duration = delivery[3]
                date = delivery[4]
                return Delivery(distance, price, duration, date, id)
        except sqlite3.Error as e:
            logging.error(f"Erreur lors de la récupération de la livraison : {e}")

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

    def get_stats(self) -> dict :
        try:
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()
                cursor.execute("""SELECT COUNT(*),
                                                SUM(distance),
                                                SUM(price),
                                                SUM(duration),
                                                AVG(distance),
                                                AVG(price),
                                                AVG(duration)
                                                FROM deliveries""")
                stats_tuple = cursor.fetchone()

                total_deliveries = stats_tuple[0]
                total_distance = stats_tuple[1] if stats_tuple[1] is not None else 0
                total_price = stats_tuple[2] if stats_tuple[2] is not None else 0
                total_duration = stats_tuple[3] if stats_tuple[3] is not None else 0
                average_distance = stats_tuple[4] if stats_tuple[4] is not None else 0
                average_price = stats_tuple[5] if stats_tuple[5] is not None else 0
                average_duration = stats_tuple[6] if stats_tuple[6] is not None else 0

        
                return {"total_deliveries": total_deliveries,
                        "total_price": total_price,
                        "total_duration": total_duration,
                        "total_distance": total_distance,
                        "average_distance": average_distance,
                        "average_price": average_price,
                        "average_duration": average_duration
                    }
               
                

        except sqlite3.Error as e:
            logging.error(f"Erreur lors de la récupération des statistiques : {e}")
            return {}


    

        



