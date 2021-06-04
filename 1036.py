import math
ask = input().split()
a, b, c = ask
b = float(b)
a = float(a)
c = float(c)

if a <= 0 and b <= 0 and c <= 0:
    print('Impossivel calcular')
else:
    # a_r = math.sqrt(a)
    # b_r = math.sqrt(b)
    # c_r = math.sqrt(c)
    # x1 = (-b + math.sqrt( (b*b)-( 4*a*c) ) )/ 2*a

    # x2 = (-b - math.sqrt( (b*b)-( 4*a*c) ) )/ 2*a
    x1 = (-b + math.sqrt((b ** 2) - 4 * a * c))*2*a
    x2 = (-b - math.sqrt((b ** 2) - 4 * a * c))*2*a


print(x1, x2)