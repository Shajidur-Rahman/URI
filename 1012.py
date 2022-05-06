a,b,c = map(float, input().split())
x1 = round(a*c*.5,3) 
x2 =  3.14159 * (c*c)
x3 = (a+b)*c*.5
x4 = b*b
x5 = a*b
print("TRIANGULO:",'%.3f' % x1)
print("CIRCULO:",'%.3f' % x2)
print("TRAPEZIO:",'%.3f' % x3)
print("QUADRADO:",'%.3f' % x4)
print("RETANGULO:",'%.3f' % x5)