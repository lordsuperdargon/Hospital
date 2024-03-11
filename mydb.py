import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Group1'

)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE Group1")

print("All Done Pal!!")