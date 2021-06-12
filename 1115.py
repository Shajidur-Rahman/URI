# 2 2
# 3 -2
# -8 -1
# -7 1
# 0 2

# primeiro
# quarto
# terceiro
# segundo
while True:
    a,b = map(float, input().split())
    if a > 0 and b > 0:
        print('primeiro')
    elif a > 0 and b < 0:
        print('quarto')
    elif a < 0 and b < 0:
        print('terceiro')
    elif a < 0 and b > 0:
        print('segundo')
    else:
        exit()