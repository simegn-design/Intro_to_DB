#!/usr/bin/python3
"""Create alxbookstore database"""

import mysql.connector
import sys

def create_database():
    """Creates the alxbookstore database"""
    try:
        # Establish connection without specifying a database
        conn = mysql.connector.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2]
        )
        
        # Create cursor
        cursor = conn.cursor()
        
        # Create database (exact name as specified)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore")
        print("Database 'alxbookstore' created successfully!")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python MySQLServer.py <mysql_username> <mysql_password>")
    else:
        create_database()
