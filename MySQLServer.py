#!/usr/bin/python
"""Create alxbookstore database"""

import MySQLdb
import sys

def create_database():
    try:
        conn = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2]
        )
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore")
        print("Database created successfully")
    except MySQLdb.Error as err:
        print(f"Error: {err}")
    finally:
        if 'conn' in locals():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python MySQLServer.py <username> <password>")
        sys.exit(1)
    create_database()
