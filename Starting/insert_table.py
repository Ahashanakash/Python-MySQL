import mysql.connector

database_name = "python_test_database"

mydbconnection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd = "nokia105ms",
    database = database_name
)

mycursor = mydbconnection.cursor()

sqlquery = """INSERT INTO Students 
            (roll, name, age) VALUES ('23','Akash',23)
            """

mycursor.execute(sqlquery)
mydbconnection.commit()
print("inserted")