ask = input().split()

a,b,c = ask

a = float(a)
b = float(b)
c = float(c)

mexof = max(a,b,c)

li = [a,b,c]
li.remove(mexof)

sumof = li[0] + li[1]
if sumof <= mexof:
    print("Area =",.5 * (a+ b) * c)
else:
    print(f"Perimetro = {a+b+c}")