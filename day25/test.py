import pandas as pd
from random import choice

state_data = pd.read_csv('day25/50_states.csv')

print(state_data[state_data.state == 'Florida'].squeeze().state)