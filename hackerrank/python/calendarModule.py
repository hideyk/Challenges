import calendar
from datetime import datetime

day, month, year = map(int, input().split())

print(calendar.day_name[datetime(day=day, month=month, year=year).weekday()].upper())

