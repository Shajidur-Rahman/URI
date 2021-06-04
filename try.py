day = int(input())

year = round(day / 360) 
day = day - 360
month = round(day / 30)
days = round(day % 360)
if days >= 30:
    days = days - 30
    month = month + 1

if month >= 12:
    month = month -12
    year = year + 1

print(year, month, days)