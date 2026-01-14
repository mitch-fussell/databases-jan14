import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

query = """
    SELECT *
    FROM points;

"""

cursor.execute(query)
#No commit function because you are extracting from the database
result = cursor.fetchall() #fetches all points instead


conn.close()


print(result)