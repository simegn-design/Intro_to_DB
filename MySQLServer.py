#!/usr/bin/python3
"""Create alx_book_store database"""

import MySQLdb
import sys

def create_database():
    try:
        conn = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            port=3306
        )
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
    finally:
        if 'conn' in locals() and conn.open:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python MySQLServer.py <mysql_username> <mysql_password>")
    else:
        create_database()
