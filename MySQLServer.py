#!/usr/bin/python3
"""DB creation script for ALX"""

import mysql.connector
from mysql.connector import Error
import sys

def create_db():
    """Create alxbookstore database"""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2]
        )
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore")
        print("Database created successfully")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python MySQLServer.py <user> <password>")
        sys.exit(1)
    create_db()
