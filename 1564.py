try:
    while True:
        a = int(input())
        if a == 0:
            print('vai ter copa!')
        else:
            print('vai ter duas!')
except EOFError as efo:
    pass