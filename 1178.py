a = float(input())
b = 0
for i in range(100):
    c = format(a, '.4f')
    print(f"N[{i}] = {c}")
    a = a / 2