
import psycopg2
try:
    connection = psycopg2.connect(dbname="udacity",user="postgres",password="Aklexsqldb14")

    cursor = connection.cursor()

    cursor.execute('SELECT * FROM hotel;')
    print("Selecting rows from table2 table using cursor.fetchall")
    

    result = cursor.fetchall()
    
    print("Print each row and it's columns values")
    
    for row in result:
        print("Hotel_ID = ", row[0], )
        print("Hotel_Name = ", row[1], )
        print("Country = ", row[2], )
        print("City = ", row[3], )
        print("Is it Five Star = ", row[4], "\n")
    # print("Getting all record", result)
    # result = cursor.fetchmany(2)
    # print("fetchMany", result)

    # result = cursor.fetchone()
    # print("fetchOne", result)
    
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