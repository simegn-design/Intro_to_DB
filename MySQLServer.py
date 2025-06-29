#!/usr/bin/python3
"""ALX Database Creation Script"""

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost', user='user', password='pass')
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore")
except Error:
    pass
