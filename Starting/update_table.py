import mysql.connector

database_name = "python_test_database"

mydbconnection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd = "nokia105ms",
    database = database_name
)

mycursor = mydbconnection.cursor()
mycursor.execute("set sql_safe_updates = 0")

sqlquery = """UPDATE Students 
                SET Name = 'Ak'
                where name = 'Akash'
            """

mycursor.execute(sqlquery)
mydbconnection.commit()
print("updated")