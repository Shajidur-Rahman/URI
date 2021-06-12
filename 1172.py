for i in range(10):
        ask = int(input())
        if ask <= 0:
            print(f"X[{i}] = 1")
        else:
            print(f"X[{i}] = {ask}")