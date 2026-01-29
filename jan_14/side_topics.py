# import pandas as pd

# my_list = [(1,2),(3,4)]

# df = pd.DataFrame(my_list, columns = ['x', 'y'])

# print(df)

#------------------------------------------------------------------------



import gradio as gr

def f(x):
    return x**2

iface = gr.Interface(
    fn = f, #function
    inputs = gr.Number(),
    outputs = gr.Number()

)

iface.launch() #control C will close the port with the application