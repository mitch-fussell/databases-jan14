import sqlite3
import gradio as gr
import pandas as pd

#function to produce list

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()

#making a subquery that creates a table called top_hitters which you can query too
#CONCAT joins the two names but needs a space in between to keep it two words
query = """
    WITH top_hitters AS (
    SELECT nameFirst, nameLast
    FROM batting INNER JOIN people
    ON batting.playerID = people.playerID
    WHERE teamID = 'PHI'
    GROUP BY batting.playerID
    ORDER BY sum(HR) DESC
    LIMIT 10
    )
    
    
    SELECT CONCAT(nameFirst, ' ', nameLast)
    FROM top_hitters
    ORDER BY nameLast ASC

"""
cursor.execute(query)
records = cursor.fetchall()
conn.close()

players = []

for record in records:
    players.append(record[0])
    
print(players)


with gr.Blocks() as iface:
    playerbox = gr.Dropdown(players, value = None, label = "Select a Phillie") #value = None is the starting value of the app
    
    
iface.launch()