import sqlite3
import gradio as gr
#import pandas as pd

#function to produce list
def fetch_phillies():
    conn = sqlite3.connect('../baseball.db')
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
    conn = sqlite3.connect('../baseball.db')
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


#opens gradio with Blocks and creates the dropdown

with gr.Blocks() as iface: #opens gradio without calling the iface() object individually
    
    #makes a box with a dropdown to select the player using the fetch_phillies() function
    playerbox = gr.Dropdown(fetch_phillies(), value = None, label = "Select a Phillie")            
    HRsumbox = gr.Number(label = 'This is the sum of the Homeruns')
    
    playerbox.change(fn = f,  inputs = [playerbox],  outputs = [HRsumbox]) #updates things if theres a change in the xbox by running the inputs through the function
   
    
iface.launch()