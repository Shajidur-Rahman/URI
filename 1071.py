x = int(input())
y = int(input())
li = []
res = [a for a in range(y, x) if a%2 != 0]
res = sum(res)
print(res)
