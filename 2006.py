a = int(input())

my = list(map(int, input().split()))

res = 0
for i in range(0,5):
    if my[i] == a:
        res = res + 1
    else:
        pass

print(res)