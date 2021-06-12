a = 0
ti = 0.2
while 10 > a:
    for i in range(1,4):
        print(f"I={0 + ti} J={i + ti} ")
    ti = ti + 0.2
    ti = format(ti, '.1f')
    ti = float(ti)
    a = a + 1



# i = 0
# j = 1
# value = 0
# temp = 0
# temp2 = 0
# while (i <= 2):
#     if (temp2 == 0):
#         print("I=%.0f J=%.0f" % (i, j))
#     else:
#         print("I=%.1f J=%.1f" % (i, j))

#     temp += 1
#     if (temp == 3):
#         i += 0.2
#         value += 0.2
#         j = value
#         temp = 0
#         temp2 += 1

#     if(temp2 == 5):
#         temp2 = 0
#     j += 1