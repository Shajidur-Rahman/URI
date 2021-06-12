while True:
    a,b = map(int, input().split())
    c = 0
    if a == 0 or a < 0 or b == 0 or b < 0 or a == b:
        exit()
    else:
        for i in range(b,a + 1):
            c = i + c
            print(i, end=' ')
    # 2 3 4 5 Sum=14
    print(f"Sum={c}")
