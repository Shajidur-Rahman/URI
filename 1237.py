while True:
    a = input()
    b = input()

    time = 0

    if len(a)>len(b):
        for i in range(0,len(b)):
            if b[i] in a:
                if b[i+1] in a:
                    time = time + 1
                elif b[i-1] in a:
                    time = time + 1
            else:
                pass
            time = time +1
    else:
        for i in range(0,len(a)):
            if a[i] in b:
                if a[i+1] in b:
                    time = time + 1
                elif a[i-1] in b:
                    time = time + 1
            else:
                pass
            time = time + 1
    print(time)