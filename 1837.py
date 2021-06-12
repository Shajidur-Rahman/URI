# a,b = map(int, input().split())
# res = (a / b)
# res = round(res)
# remin = (a % b)
# remin = round(remin)
# print(res, remin)


a, b = [int(x) for x in input().split()]
for r in range(abs(b)):
    if ((a - r) % b) == 0:
        q = int((a - r)/b)
        break
print(q, r)