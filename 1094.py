a = int(input())
c = 0
r = 0
s = 0
for i in range(a):
    a, ch = list(input().split())
    ch.lower()
    a = int(a)
    if ch == 'c':
        c = c + a
    elif ch == 'r':
        r = r + a
    elif ch == 's':
        s = s + a
total = c+r+s
Total = f"Total: {c + r + s} cobaias"
C = f"Total de coelhos: {c}"
R = f"Total de ratos: {r}"
S = f"Total de sapos: {s}"
CP = f"Percentual de coelhos: {(c * 100) / total} %"
RP = f"Percentual de ratos: {(r * 100) / total} %"
SP = f"Percentual de sapos: {(s * 100) / total} %"
print(C)
print(R)
print(S)
print(CP)
print(RP)
print(SP)