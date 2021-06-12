a = int(input())
for i in range(a):
    ask = int(input())
    if ask == 0:
        print('NULL')
    elif ask%2 == 0 and ask > 0:
        print('EVEN POSITIVE')
    elif ask%2 == 0 and ask < 0:
        print('EVEN NEGATIVE')
    elif ask%2 != 0 and ask > 0:
        print('ODD POSITIVE')
    elif ask%2 != 0 and ask <0:
        print('ODD NEGATIVE')
    else:
        pass