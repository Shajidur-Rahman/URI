days = int(input())

month = days / 30
if days > 360:
    a = month - 12
    month = month + a + 1

year = month / 12
year = round(year)

month = month % 12
month = round(month)


day = days % 360
day = round(day)


if day > 30:
    day = day - 30
    month = month + 1

print(f"year {year}, month {month}, day{day}")