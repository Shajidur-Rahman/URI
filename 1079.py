# ((6.5×2) + (4.3 × 3) + (6.2× 5) ) ÷10
try:
    a,b,c = map(float, input().split())
    res = format((((a * 2 )+(b * 3 )+(c * 5 )) / 10), '.1f')
    print(res)
except:
    pass