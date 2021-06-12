try:
    li = []
    while True:
        a = int(input())
        for i in range(1,a + 1):
            if a == 0:
                exit()
            else:
                li.append(i)

        for i in li:
            print(i, end=' ')
        li.clear()
except EOFError as efo:
    pass