import sqlite3
import gradio as gr
import pandas as pd

#function to produce list
def fetch_phillies():
    conn = sqlite3.connect('baseball.db')
    cursor = conn.cursor()
    query = """
        SELECT playerID
        FROM batting
        WHERE teamID = 'PHI' AND yearID = 1976
    
    """
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    
    players = []
    
    for record in records:
        players.append(record[0])
    return players
    
    #records = pd.DataFrame(records, columns = ["playerID"])

def f(player):
    conn = sqlite3.connect('baseball.db')
    cursor = conn.cursor()
    query = """
        SELECT HR
        FROM batting
        WHERE teamID = 'PHI' AND yearID = 1976 AND playerID = ?
    
    """
    cursor.execute(query, [player]) #[player] inputs each player into ? because the query is in a string
    records = cursor.fetchall()
    conn.close()
    
    return records[0][0] #[0][0] gets the first record and gets the first element of that record


      


iface = gr.Interface(fn = f, inputs = gr.Dropdown(fetch_phillies(), value = None), outputs = "number", live = True)

iface.launch()
