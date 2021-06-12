# d=0
# c=0
# while(True):
#     try:
#         if(d==2):
#             break
#         a = float(input())
#         if(a>=0 and a<=10):
#             d=d+1
#             c=c+a
#         else:
#             print("nota invalida")
#     except EOFError:
#         break
# b=c/2.00
# print("media = %0.2f"%b)

p = 0
c = 0
while p < 2:
    a = float(input())
    if a >= 0 and a <= 10:
        c = c + a
        p = p + 1
    else:
        print("nota invalida")

b = c / 2.00
b = format(b, '.2f')
print(f'media = {b}')