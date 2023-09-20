import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'marce',
    passwd = 'p3rm1s00'
)

# Prepare a cursor object

cursorObject = dataBase.cursor()

# Create a DB

cursorObject.execute("CREATE DATABASE db")

print('All Done!')