import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_the_week = now.weekday()

# print(day_of_the_week)

date_of_birth = dt.datetime(year=1995, month=11, day=8, hour=6)
print(date_of_birth)