
import psycopg2
try:
    connection = psycopg2.connect(dbname="udacity",user="postgres",password="Aklex@sqldb14")

    cursor = connection.cursor()

    cursor.execute('SELECT * FROM table2;')
    print("Selecting rows from table2 table using cursor.fetchall")
    

    result = cursor.fetchall()
    
    print("Print each row and it's columns values")
    
    for row in result:
        print("ID = ", row[0], )
        print("fName = ", row[1], )
        print("lName = ", row[2], )
        print("phone = ", row[3], )
        print("completed = ", row[4], "\n")
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