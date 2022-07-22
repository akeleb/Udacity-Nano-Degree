import psycopg2

connection = psycopg2.connect(dbname="udacity",user="postgres",password="Aklex@sqldb14")

cursor = connection.cursor()

cursor.execute('SELECT * FROM table2;')
result = cursor.fetchall()
print(result)

connection.commit()

connection.close()
cursor.close()