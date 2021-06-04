ask = input().split()
a, b, c = ask
a = int(a)
b = int(b)
c = int(c)
# first
li = [a,b,c]
li.sort()
# second 
li2 = [a,b,c]
li2.sort(reverse=True)


# main
for i in li:
    print(i)
print('')
for i2 in li2:
    print(i2)