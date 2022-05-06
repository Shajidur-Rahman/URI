a = int(input())

year = 0
month = 0
day = 0

while a >= 365:
    year = year+1
    a = a -365
while a>=30:
    month = month+1
    a = a-30
day = a
print(f"{year} ano(s)")
print(f"{month} mes(es)")
print(f"{day} dia(s)")