#!/usr/bin/python3
"""ALX Bookstore Database Creator"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish connection
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Will be replaced by sys.argv in final version
            password=""
        )
        
        # Create cursor and execute
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore")
        print("Database created successfully")
        
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
