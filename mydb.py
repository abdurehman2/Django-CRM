# Install MYSql on computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python
import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root123',
    )   

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE DjangoDB")

print("Database created successfully!")