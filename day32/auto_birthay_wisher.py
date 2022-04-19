import datetime as dt
import smtplib
import pandas as pd

host = 'smtp.gmail.com'
my_email = 'test.dev.08.1995@gmail.com'
password = 'azerty77!!'
receiver = 'invisiman042@gmail.com'

birthdays = pd.read_csv('day32/birthdays.csv')

def send_email(host, my_email, password, receiver, message):

    with smtplib.SMTP(host, 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=receiver,
            msg=message,
            )

now = dt.datetime.now()
today_tup = (now.month, now.day)

birthdays = {(data_row['month'], data_row['day']) : data_row for (index, data_row) in birthdays.iterrows()}

for birthday in birthdays:
    birthday_person = birthdays[today_tup]
    if birthday == today_tup:
        print(f'it\'s {birthday_person.person_name} birthday today')

        with open('day32/letter.txt') as file:
            letter = file.read()
            message = letter.replace('[name]', str(birthday_person.person_name))

        send_email(host, my_email, password, receiver, message)