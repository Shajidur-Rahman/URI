# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# fir = c + d
# se = a + b
# even = a%2

# if b > c and d > a and fir > se and c > 0 and d > 0 and even == 0:
#     print('Valores aceitos')
# else:
#     print('Valores nao aceitos')

ask = input().split()

a,b,c,d = ask
a = int(a)
b = int(b)
c = int(c)
d = int(d)
fir = c + d
se = a + b
even = a%2


if b > c and d > a and fir > se and c > 0 and d > 0 and even == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')