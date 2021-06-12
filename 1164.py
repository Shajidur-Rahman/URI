time = int(input())
c = 0
while time > c:
    c = c + 1
    a = int(input())
    li = []
    for i in range(1, a):
        if a%i == 0:
            li.append(i)
        else:
            pass
    sumof = sum(li)
    if sumof == a:
        print(f"{a} eh perfeito")
    else:
        print(f'{a} nao eh perfeito')