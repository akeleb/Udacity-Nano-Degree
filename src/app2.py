import psycopg2
try:
  connection = psycopg2.connect(
      dbname="udacity", user="postgres", password="Aklex@sqldb14")

  cursor = connection.cursor()

  cursor.execute('DROP TABLE IF EXISTS table2;')

  cursor.execute('''
    CREATE TABLE table2 (
      id INTEGER PRIMARY KEY,
      fName VARCHAR(20),
      lName Varchar(20),
      Phone VARCHAR(20),
      completed BOOLEAN NOT NULL DEFAULT False
    );
  ''')

  cursor.execute('INSERT INTO table2 (id, fName,lName,phone, completed) VALUES (%s, %s,%s,%s,%s);',
                (1, 'Akele', 'Belay', '0929430828', True))

  cursor.execute('INSERT INTO table2 (id, fName,lName,phone, completed) VALUES (%s, %s,%s,%s,%s);',
                (2, 'Noli', 'Fantahun', '0924430828', True))

  SQL = 'INSERT INTO table2 (id, fName,lName,phone, completed) VALUES (%(id)s,%(fName)s, %(lName)s,%(phone)s, %(completed)s);'

  data = {
      'id': 3,
      'fName': 'Betty',
      'lName': 'AkeleK',
      'phone': '0918273329',
      'completed': False
  }

  cursor.execute(SQL, data)

  connection.commit()

  connection.close()
  cursor.close()
except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
