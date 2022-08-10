import psycopg2
try:
  connection = psycopg2.connect(
      dbname="udacity", user="postgres", password="Aklexsqldb14")

  cursor = connection.cursor()

  cursor.execute('DROP TABLE IF EXISTS hotel;')

  cursor.execute('''
    CREATE TABLE hotel (
      HOTEL_ID  SERIAL PRIMARY KEY,
      Name VARCHAR(20),
      Country Varchar(20),
      City VARCHAR(20),
      FiveStar BOOLEAN NOT NULL DEFAULT False
    );
  ''')

  cursor.execute('INSERT INTO hotel (HOTEL_ID, Name,Country, City,FiveStar) VALUES (%s, %s,%s,%s,%s);',
                (1, 'Skylight', 'Ethiopia', 'Addis Ababa',True))


  SQL = 'INSERT INTO hotel (HOTEL_ID, Name,Country,City, FiveStar) VALUES (%(HOTEL_ID)s,%(Name)s, %(Country)s,%(City)s, %(FiveStar)s);'

  data = {
      'HOTEL_ID': 2,
      'Name': 'Radison Blu',
      'Country': 'Ethiopia',
      'City': 'Addis Ababa',
      'FiveStar': True
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
