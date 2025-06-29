#!/usr/bin/python3
import mysql.connector
cursor = mysql.connector.connect(host='x',user='x',password='x').cursor()
cursor.execute("CREATE DATABASE alxbookstore")
