from datetime import datetime, timedelta

day, month, year = map(int, input().split())

print((datetime(year=year, month=month, day=day)-timedelta(days=2)).strftime("%A").upper())
