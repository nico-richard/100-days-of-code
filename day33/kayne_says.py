from tkinter import *

from pyparsing import col
import requests

def get_quote():
    global kanye_quote
    response = requests.get(url='https://api.kanye.rest')
    quote = response.json()['quote']
    canvas_quote.itemconfig(kanye_quote, text=quote
    )

window = Tk()
window.title('Kayne says')
window.config(padx=50, pady=50, bg='#ffffff')

canvas_quote = Canvas(width=300, height=414, bg='#ffffff', highlightthickness=0)
button_kanye = Button(relief='flat', bg='#ffffff', highlightthickness=0, command=get_quote)

kanye_face = PhotoImage(file='day33/data/kanye.png')
quote_bg = PhotoImage(file='day33/data/background.png')

canvas_quote.create_image(0, 0, image=quote_bg, anchor='nw')
button_kanye.config(image=kanye_face)
kanye_quote = canvas_quote.create_text(150, 207, text='', width=250, font=('Ariel', 25, 'bold'))

canvas_quote.grid(row=0, column=0)
button_kanye.grid(row=1, column=0)

window.mainloop()