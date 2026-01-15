import sqlite3
import gradio as gr
import pandas as pd

def fetch_points():
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

    df = pd.DataFrame(result, columns = ['id', 'x', 'y'])


    return df

iface = gr.Interface(
    fn = fetch_points,
    inputs = [],
    outputs = gr.LinePlot(x = 'x', y = 'y', x_lim = (0,7), y_lim = (0,15))

)

iface.launch()