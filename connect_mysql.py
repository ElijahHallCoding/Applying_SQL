# Establishing the Connection

import mysql.connector
from mysql.connector import Error

def connect_database():
    """ COnnect to the MySQL database and return the connection object """

    #Database connection parameters 
    db_name = "e_commerce_db"
    user = "root"
    password = "Daniel10@@@@"
    host = "localhost"

    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        # Check if the connection si sucessful
        print("Connected to MySQL database successfully")
        return conn
    
    except Error as e:
        # Handling any connection errors
        print(f"Error: {e}")
        return None