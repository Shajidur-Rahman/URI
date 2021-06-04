num = float(input())
if num < 0 or num > 100:
    print('Fora de intervalo')
elif num <= 25:
    print(f'Intervalo [0,{int(num)}]')
elif num >= 25 and num < 50:
    print(f'Intervalo [25,50]')
elif num >= 50 and num < 75:
    print(f'Intervalo [50,75]')

else:    print(f'Intervalo [75,100]')

# elif num > 50 and nu < 75:
#     print(f'Intervalo [50,{num}]')
