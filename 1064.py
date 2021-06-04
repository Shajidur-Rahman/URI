a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
li = [a, b, c, d, e, f]
positive = [x for x in li if x >= 0]
res = len(positive)
print(f"{res} valores positivos")
sumof = sum(positive) / res
print(f'{sumof}')