import smtplib
from random import choice
import pandas as pd
import datetime as dt

host = 'smtp.gmail.com'
my_email = 'test.dev.08.1995@gmail.com'
password = 'azerty77!!'
receiver = 'invisiman042@gmail.com'

now = dt.datetime.now()

with open('day32/quotes.txt') as file:
    quote_list = file.readlines()

chosen_quote = choice(quote_list)
message = f'Subject:Monday quote\n\n{chosen_quote}'

def send_email(host, my_email, password, receiver, message):

    with smtplib.SMTP(host, 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=receiver,
            msg=message,
            )

if now.weekday() == 0:
    send_email(host, my_email, password, receiver, message)
    print('email sent')