a = int(input())
for i in range(a):
    ask = int(input())
    if ask == 0:
        askfor = ask
    else:
        askfor = ask -1
    print(f"Fib({ask}) = {askfor}")