import mysql.connector

mydbconnection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "nokia105ms"
)
print(mydbconnection)

database_name = "python_test_database"

mycursor = mydbconnection.cursor()

sqlquery = "CREATE DATABASE " + database_name 

mycursor.execute(sqlquery)
print("database craeted successfully")