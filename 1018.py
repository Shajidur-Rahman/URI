a = int(input())
b = a
a100 = 0
a50 = 0
a20 = 0
a10 = 0
a5 = 0
a2 = 0
a1 = 0

if a//100 >= 0:
    a100 = a//100
    a = a-100*a100
if a//50 >= 0:
    a50 = a//50
    a = a-50*a50
if a//20 >= 0:
    a20 = a//20
    a = a-20*a20
if a//10 >= 0:
    a10 = a//10
    a = a-10*a10
if a//5 >= 0:
    a5 = a//5
    a = a-5*a5
if a//2 >= 0:
    a2 = a//2
    a = a-2*a2
if a//1 >= 0:
    a1 = a//1
    a = a-1*a1

print(b)
print(f"{a100} nota(s) de R$ 100,00")
print(f"{a50} nota(s) de R$ 50,00")
print(f"{a20} nota(s) de R$ 20,00")
print(f"{a10} nota(s) de R$ 10,00")
print(f"{a5} nota(s) de R$ 5,00")
print(f"{a2} nota(s) de R$ 2,00")
print(f"{a1} nota(s) de R$ 1,00")