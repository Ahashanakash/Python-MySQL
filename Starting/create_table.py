import mysql.connector

database_name = "python_test_database"

mydbconnection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "nokia105ms",
    database = database_name
)

mycursor = mydbconnection.cursor()

sqlquery = """CREATE TABLE Students (
            roll varchar(50),
            name varchar(50),
            age int
            )"""

mycursor.execute(sqlquery)
print("Create table successfully")