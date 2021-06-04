x = int(input())
li = []
res = [a for a in range(x, x + 12) if a%2 != 0]
for i in res:
    print(i)