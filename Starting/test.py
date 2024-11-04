import mysql.connector

mydbconnection = mysql.connector.connect(
    host = "localhost",
    user="root",
    passwd = "nokia105ms"
)
print(mydbconnection)