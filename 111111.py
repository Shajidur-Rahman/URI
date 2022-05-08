from cgi import print_arguments
from datetime import datetime


a,b,c,d = map(int, input().split())

s1 = f'{a}:{b}'
s2 = f'{c}:{d}'

FMT = '%H:%M'

tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
tdleta2 = str(tdelta)



x,y,z = tdleta2.split(":")

if int(x)==0 and int(y)==0:
    print(f"O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")

else:

    print(f"O JOGO DUROU {int(x)} HORA(S) E {int(y)} MINUTO(S)")