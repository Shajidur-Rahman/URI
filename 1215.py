import re
 
test_string = input()

test_string = test_string.lower() 

res = re.findall(r'\w+', test_string)

res.sort()

final = set()


for a in res:
    final.add(a)

res.clear()

for b in final:
    res.append(b)

res.sort()

for i in res:
    print(i)