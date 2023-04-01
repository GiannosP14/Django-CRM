import mysql.connector

dataBase = mysql.connector.connect (
host = 'localhost',
user = 'root',
passwd = 'rootmaria14'
)

#prepare cursor obj
cursorObject = dataBase.cursor()

#Create a db
cursorObject.execute("CREATE DATABASE IF NOT EXISTS elderco")
print("All Done!")