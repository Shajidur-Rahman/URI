# test = int(input())
# for i in range(test):
#     ask = input()
#     if ask == "P=NP":
#         print('skipped')
#     else:
#         a,b = ask.split('+')
#         a = int(a)
#         b = int(b)
#         print(a + b)



S = input()
fir = S[0]
las = S[-1]
if fir == las:
	print('Yes')
else:
	print('No')