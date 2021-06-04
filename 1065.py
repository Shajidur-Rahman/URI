a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
li = [a,b,c,d,e]
even = [x for x in li if x % 2==0]
print(f"{len(even)} valores pares")