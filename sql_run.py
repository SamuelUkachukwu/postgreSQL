# import psycopg2 at the top of the file
import psycopg2


# then let psycopg2 connect to the postgre database using the .connect() method
# and we will assign it a variable of any name you chose.
# specify the name of the database e.g psycopg2.connect(database="chinook")
connecting = psycopg2.connect(database="chinook")

# Open a cursor to perform database operations
# build a cursor object of the database
cursor = connecting.cursor()

# Query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - select all tracks where the composer is "Queen" from the "Track" table
# cursor.execute(
#     'SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"]
#     )

cursor.execute(
    'SELECT * FROM "Track" WHERE "Composer" = %s', ["Be"]
    )

# fetch the result(multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the connection
# Close communication with the database
connecting.close()

# print result
for result in results:
    print(result)
