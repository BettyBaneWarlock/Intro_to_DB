# MySQLServer.py

import mysql.connector
from mysql.connector import errorcode

def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")

def connect_to_mysql():
    try:
        # Connect to MySQL Server
        connection = mysql.connector.connect(
            host="localhost",       # Update with your host
            user="root",            # Update with your username
            password="your_password" # Update with your password
        )

        if connection.is_connected():
            print("Connected to MySQL server")
            cursor = connection.cursor()
            create_database(cursor)
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
        else:
            print("Failed to connect to MySQL server")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Access denied: Check your username and password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(f"Error: {err}")

if __name__ == "__main__":
    connect_to_mysql()

