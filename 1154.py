t = 0
c = 0
while True:
    ask = int(input())
    if ask < 0:
        break
    else:
        c = ask + c
        t = t + 1
res = c/t
res = format(res, '.2f')
print(res)