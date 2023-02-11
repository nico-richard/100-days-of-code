from tkinter import *
from tkinter import messagebox
import string
from random import shuffle, choice
import pyperclip
import json

WHITE = '#ffffff'
PASSWORD_LENGTH = 15

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    characters = list(string.ascii_letters + string.digits + '@[]^_!"#$%&\'()*+,-./:;{}<>=|~?')
    shuffle(characters)
    password = [choice(characters) for i in range(PASSWORD_LENGTH + 1)]
    shuffle(password)
    password = ''.join(password)
    password_entry.delete(0, END)
    password_entry.insert(END, string=password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_credential = {
        website:{
            "username" : username,
            "password" : password,
        }
    }

    if len(website) == 0 or  len(password) == 0:
        messagebox.showinfo(
            title='Error',
            message='Informations are missing',
        )

    elif messagebox.askokcancel(
        title='Confirmation',
        message=f'Do you confirm this new credential entry ?\n\nWebsite : {website}\nUsername : {username}\nPassword : {password}',
        ):

        try:
            with open('day29/credentials.json', 'r') as data_file:
                data = json.load(data_file)
                data.update(new_credential)
        except (json.decoder.JSONDecodeError, FileNotFoundError):
            with open('day29/credentials.json', 'w') as data_file:
                json.dump(new_credential, data_file, indent=4)
        else:
            with open('day29/credentials.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        
        finally:
            pyperclip.copy(password)

            messagebox.showinfo(
                title='Information',
                message='The credential has been saved\n(the password has been copied to clipboard)',
                )
            
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    file_name = 'day29/credentials.json'
    try:
        with open(file_name, 'r') as data_file:
            data = json.load(data_file)
            website_requested = website_entry.get()
            credentials = data[website_requested]

    except (json.decoder.JSONDecodeError, FileNotFoundError):
        messagebox.showinfo(
                title='Information',
                message=f'There is no or empty file : {file_name} containing passwords',
                )
    except KeyError:
        messagebox.showinfo(
                title='Information',
                message='There is no password for this website',
                )    
    else:
        messagebox.showinfo(
                title='Information',
                message=(f'There are the credentials for {website_requested} :\n\n'
                f'Username : {credentials["username"]}\nPassword : {credentials["password"]}'),
                )
        pyperclip.copy(credentials["password"])

    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password manager')
window.config(padx=40, pady=40)
window.config(bg=WHITE)

image = PhotoImage(file='day29/logo.png')
IMG_WIDTH = image.width()
IMG_HEIGHT = image.height()

canvas = Canvas(width=IMG_WIDTH, height=IMG_HEIGHT)
canvas.create_image(IMG_WIDTH / 2, IMG_HEIGHT / 2, image=image)
canvas.grid(row=0, column=1, pady=(0, 20))
canvas.config(bg=WHITE, highlightthickness=0)

# Widget creation
website_label = Label(text='Website :', bg=WHITE)
username_label = Label(text='Username / Email :', bg=WHITE)
password_label = Label(text='Password :', bg=WHITE)

website_entry = Entry(bg=WHITE)
username_entry = Entry(bg=WHITE)
password_entry = Entry(bg=WHITE)

generate_password_button = Button(text='Generate password', bg=WHITE, relief='groove', command=gen_password)
add_password_button = Button(text='Add new password', bg=WHITE, relief='groove', command=save_password)
search_password_button = Button(text='Search', bg=WHITE, relief='groove', command=search_password)

# Grid placement
website_label.grid(row=1, column=0, sticky='e')
username_label.grid(row=2, column=0, sticky='e')
password_label.grid(row=3, column=0, sticky='e')

website_entry.grid(row=1, column=1, sticky='ew')
website_entry.focus()
username_entry.grid(row=2, column=1, columnspan=2, sticky='ew')
username_entry.insert(END, string='nicolas.richard42@hotmail.fr')
password_entry.grid(row=3, column=1, sticky='ew')

generate_password_button.grid(row=3, column=2, padx=(5, 0), sticky='ew')
add_password_button.grid(row=4, column=1, columnspan=2, sticky='ew')
search_password_button.grid(row=1, column=2, padx=(5, 0), sticky='ew')

window.mainloop()