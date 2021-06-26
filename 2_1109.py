while True:
    result = input()
    result.replace('(', '')
    time = int(input())
    if '.' in result:
        a,b = result.split('.')
        result = a+b
        result = result.split('(')
        print(result)

    for i in range(time):
        ask = input()
        if result in ask:
            print("Y")
        else:
            print("N")