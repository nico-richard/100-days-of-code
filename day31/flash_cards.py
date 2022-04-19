from tkinter import *
from PIL import Image, ImageTk
from random import choice
import pandas as pd
import csv

BACKGROUND_COLOR = "#B1DDC6"
WHITE = '#ffffff'
BLACK = '#000000'
WORD_FONT = ('Ariel', 60, 'bold')
LANGUAGE_FONT = ('Ariel', 40, 'italic')

window = Tk()
window.title('Language learning tool')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

WINDOW_WIDTH = window.winfo_width()
WINDOW_HEIGHT = window.winfo_height()

# Function creation
def initial_setup():
    global list_of_words, current_card, list_of_learned_words, flip_timer
    '''
    - Select the data file on which words will be picked on
    - Check if there is already learned and to learn files
    '''
    try:
        # check if an file already exists
        data_to_learn = pd.read_csv('day31/data/words_to_learn.csv')
    except FileNotFoundError:
        # else read the default file
        data_to_learn = pd.read_csv('day31/data/french_words.csv')
    
    list_of_words = data_to_learn.to_dict(orient='records')

    try:
        # check if an file already exists
        data_learned = pd.read_csv('day31/data/words_learned.csv')
        list_of_learned_words = data_learned.to_dict(orient='records')
    except FileNotFoundError:
        # else read the default file
        list_of_learned_words = []
    
    current_card = {}

    update_counters()

    flip_timer = window.after(1000, flip_card)

def next_card():
    '''
    Generate a new card
    '''
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(list_of_words)

    # change card color and font
    card_canvas.itemconfig(word_text, text=current_card['French'], fill=BLACK)
    card_canvas.itemconfig(language_text, text='French', fill=BLACK)
    card_canvas.itemconfig(bg_image, image=front_card_image)

    update_counters()
    flip_timer = window.after(1000, flip_card)

def update_counters():
    '''
    Update the remaining and learned words
    '''
    words_to_learn_label.config(text=f'Words to learn : {len(list_of_words) - 1}')
    words_learned_label.config(text=f'Words learned : {len(list_of_learned_words)}')

def flip_card():
    '''
    Flip the card to its translation
    '''
    try:
        card_canvas.itemconfig(word_text, text=current_card['English'], fill=WHITE)
    except KeyError:
        pass
    else:
        card_canvas.itemconfig(word_text, fill=WHITE)
        card_canvas.itemconfig(language_text, text='English', fill=WHITE)
        card_canvas.itemconfig(bg_image, image=back_card_image)

def is_known():
    '''
    Set the current word to know, remove it from the list
    '''
    global list_of_learned_words

    if current_card in list_of_words:
        list_of_words.remove(current_card)
        list_of_learned_words.append(current_card)

    data_to_learn = pd.DataFrame(list_of_words)
    data_to_learn.to_csv('day31/data/words_to_learn.csv', index=False)

    data_learned = pd.DataFrame(list_of_learned_words)
    data_learned.to_csv('day31/data/words_learned.csv', index=False)

    next_card()

# Image importation
front_card_image = PhotoImage(file='day31/images/card_front.png')
back_card_image = PhotoImage(file='day31/images/card_back.png')
right_image = PhotoImage(file='day31/images/right.png')
wrong_image = PhotoImage(file='day31/images/wrong.png')

# Widget creation
card_canvas = Canvas(bg=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0)

words_learned_label = Label(text='Words learned : 0', bg=BACKGROUND_COLOR, highlightthickness=0,)
words_to_learn_label = Label(text='Words remaining : 0', bg=BACKGROUND_COLOR, highlightthickness=0,)

bg_image = card_canvas.create_image(800 / 2, 526 / 2, image=front_card_image)
word_text = card_canvas.create_text(800 / 2, 526 / 2.5, text='Word', font=WORD_FONT)
language_text = card_canvas.create_text(800 / 2, 526 / 1.5, text='language', font=LANGUAGE_FONT)

right_button = Button(bg=BACKGROUND_COLOR,
                    image=right_image,
                    highlightthickness=0,
                    relief='flat',
                    command=is_known,
                    )
wrong_button = Button(bg=BACKGROUND_COLOR,
                    image=wrong_image,
                    highlightthickness=0,
                    relief='flat',
                    command=next_card,
                    )

# select input words
initial_setup()

# Widget grid
card_canvas.grid(row=0, column=0, columnspan=2)
right_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)
words_learned_label.grid(row=2, column=0)
words_to_learn_label.grid(row=2, column=1)

window.mainloop()