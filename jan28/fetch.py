import sqlite3
import pandas as pd

conn = sqlite3.connect("../baseball.db")
cursor = conn.cursor()

query = """
    SELECT playerID, sum(HR)
    FROM batting
    GROUP BY playerID
    ORDER BY sum(HR) DESC
    LIMIT 10


"""

cursor.execute(query)
records = cursor.fetchall()
conn.close()

records_df = pd.DataFrame(records)
print(records_df)