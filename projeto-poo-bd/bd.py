import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "vitor133",
    database = "vendas"
)

cursor = mydb.cursor()

cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)