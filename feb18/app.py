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
    SELECT batting.playerID, nameFirst, nameLast
    FROM batting INNER JOIN people
    ON batting.playerID = people.playerID
    WHERE teamID = 'PHI'
    GROUP BY batting.playerID
    ORDER BY sum(HR) DESC
    LIMIT 10
    )
    
    
    SELECT CONCAT(nameFirst, ' ', nameLast), playerID
    FROM top_hitters
    ORDER BY nameLast ASC

"""
cursor.execute(query)
records = cursor.fetchall()
conn.close()

#players = []

# for record in records:
#     players.append(record[0])
    
def f(playerID):
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    query = """
        SELECT CAST(yearID as text), HR
        FROM batting
        WHERE teamID = 'PHI' and playerID = ?
        ORDER BY yearID
    
    """
    cursor.execute(query, [playerID]) #[player] inputs each player into ? because the query is in a string
    records = cursor.fetchall()
    conn.close()
    
    df = pd.DataFrame(records, columns = ["year", "home runs"])
    
    return df



with gr.Blocks() as iface:
    name_box = gr.Dropdown(records, interactive = True) #value = None is the starting value of the app
    plot = gr.LinePlot(x = 'year', y = 'home runs')
    name_box.change(fn = f, inputs = [name_box], outputs = [plot])
    
iface.launch()