ask = input().split()
a,b = ask
a = float(a)
b = float(b)

# main part 
if a == 0 and b == 0:
    print('Origem')
elif a == 0:
    print('Eixo X')
elif b == 0:
    print('Eixo Y')
elif a > 0 and b > 0:
    print('Q1')
elif a < 0 and b > 0:
    print('Q2')
elif a < 0 and b < 0:
    print('Q3')
elif a > 0 and b < 0:
    print('Q4')