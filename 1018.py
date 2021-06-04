time = int(input())
# time = 556

second = time % 60 # got the second


minute = time / 60
minute = time - round(minute) # got the minute

hour = time / 3600
hour = round(hour)


print(minute)
print(hour)