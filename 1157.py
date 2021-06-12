a = int(input())
lista = []
for i in range(1, a + 1):
    if a%i == 0:
        lista.append(i)
for li in lista:
    print(li)