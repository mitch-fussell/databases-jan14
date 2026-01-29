import sqlite3

conn = sqlite3.connect('my_database.db')

cursor = conn.cursor()

#Triple qoutes allow you to write on different lines with no error
query = """
    CREATE TABLE IF NOT EXISTS points(
        id INTEGER PRIMARY KEY,
        x REAL, -- Real acts the same as a Float
        y REAL
    ); -- Good practice in SQL to add ; at the end 
"""

cursor.execute(query)
conn.commit()
conn.close()
