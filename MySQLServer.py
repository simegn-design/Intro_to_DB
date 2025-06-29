#!/usr/bin/python3
"""Create alxbookstore database"""

import mysql.connector
from mysql.connector import Error
import sys

def create_database():
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2]
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database (using exact required name)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore")
            print("Database 'alxbookstore' created successfully!")
            
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python MySQLServer.py <mysql_username> <mysql_password>")
    else:
        create_database()
