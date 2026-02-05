import sqlite3
import pandas as pd

#create a connection
conn = sqlite3.connect("baseball.db")
cursor = conn.cursor()

#reading file in with pandas
df = pd.read_csv('people.csv')

df.to_sql('people', conn, if_exists = 'replace', index = False)

conn.commit()
conn.close()