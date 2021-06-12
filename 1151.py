num = int(input())
a = 0
li = [a]
b = 0
while li[-1] < num:
    li.append(a + b)
    b = b + 1
print(li)