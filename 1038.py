ask = input().split()
x,y = ask
x = int(x)
y = int(y)
if x == 1:
    res1 = format(4.00 * y, '.2f')
    print(f"Total: R$ {res1}")
elif x == 2:
    res2 = format(4.50 * y, '.2f')
    print(f"Total: R$ {res2}")
elif x == 3:
    res3 = format(5.00 * y, '.2f')
    print(f"Total: R$ {res3}")
elif x == 4:
    res4 = format(2.00 * y, '.2f')
    print(f"Total: R$ {res4}")
elif x == 5:
    res5 = format(1.50 * y, '.2f')
    print(f"Total: R$ {res5}")
