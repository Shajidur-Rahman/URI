# a = int(input())
# for i in range(a):
#     ask = int(input())
#     if ask == 2:
#         print('2 eh primo') 
#     elif ask == 7:
#         print('7 eh primo') 
#     elif ask==3:
#         print('3 eh primo') 
#     elif ask ==5:
#         print('5 eh primo') 
#     elif ask == 11:
#         print('11 eh primo')

#     elif ask%2 != 0 and ask%3 != 0 and ask%5 != 0 and ask%7 != 0 and ask%11 !=0 :
#         print(f'{ask} eh primo')
#     else:
#         print(f'{ask} nao eh primo')


a = int(input())
for i in range(a):
    ask = int(input())
    status = True
    li = [3,5,7,11]
    for x in range(2,20):
        for y in li:
            if ask%y != 0:
                # print(f'{ask} eh primo')
                status = True
            else:
                # print(f'{ask} nao eh primo')
                status = False
    if status == True:
        print(f'{ask} eh primo')
    else:
        print(f'{ask} nao eh primo')
