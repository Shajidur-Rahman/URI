a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

num = [a,b,c,d,e]
even = [x for x in num if x % 2 == 0]
even = len(even)
odd = [x for x in num if x % 2 != 0]
odd = len(odd)
positive = [x for x in num if x > 0]
positive = len(positive)
negative = [x for x in num if x < 0]
negative = len(negative)

print(f"{even} valor(es) par(es)")
print(f"{odd} valor(es) impar(es)")
print(f"{positive} valor(es) positivo(s)")
print(f"{negative} valor(es) negativo(s)")