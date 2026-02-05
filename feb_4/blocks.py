import gradio as gr

def f(x,y):
    return x + y

with gr.Blocks() as iface: #opens gradio without calling the iface() object individually
    with gr.Row():
        with gr.Column():
            xbox = gr.Number(label = "Type in a number")
            ybox = gr.Number(label = "Type in a number")
            
            
        with gr.Column():
            sumbox = gr.Number(label = 'This is the sum of those numbers')
    

    
    xbox.change(fn = f,  inputs = [xbox,ybox],  outputs = [sumbox]) #updates things if theres a change in the xbox by running the inputs through the function
    ybox.change(fn = f,  inputs = [xbox,ybox],  outputs = [sumbox]) #updates things if theres a change in the ybox
    
iface.launch()
    