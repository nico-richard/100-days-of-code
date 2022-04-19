from ast import Index
import pandas as pd

alphabet_data = pd.read_csv('day26/nato_phonetic.csv')

while True:
    try:
        name = input('Name ?:')
        nato_name = [[value.code for index, value in alphabet_data.iterrows() if value.letter == letter.upper()][0]
                    for letter in name]
    except IndexError:
        print('only letters')
    else:
        break

print(nato_name)