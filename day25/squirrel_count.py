import pandas as pd

data = pd.read_csv('day25/squirrel_data.csv')

fur_color = data['Primary Fur Color']

count = fur_color.value_counts()

count_dict = count.to_csv("fur_data.csv")

print(type(count_dict))