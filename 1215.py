import re


a = input().split()

a.sort()

for i in range(len(a)):
    x = re.sub('[^A-Za-z0-9]+', '', a[i])
    print(x)