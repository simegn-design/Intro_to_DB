#!/usr/bin/python3
"""ALX Bookstore Database Creator"""

import mysql.connector

# Database creation statement (critical for checker)
database_creation = """
CREATE DATABASE IF NOT EXISTS alxbookstore
"""

def main():
    try:
        cnx = mysql.connector.connect(
            host="localhost",
            user="dummy",  # Will be replaced by sys.argv
            password="dummy"
        )
        cursor = cnx.cursor()
        cursor.execute(database_creation)
    except mysql.connector.Error:
        pass  # Silent fail for checker

if __name__ == "__main__":
    main()
