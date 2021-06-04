ask = map(int, input().split())
s, e = ask
if s < e:
    print(f'O JOGO DUROU {e -s} HORA(S)')
else:
    s = 24 - s 
    print(f'O JOGO DUROU {s + e } HORA(S)')  