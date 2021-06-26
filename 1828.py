# # pedra = rock
# # papel =  paper
# # tesoura =  scissors
# # lagart =  lizard
# # Spock = Spock

# # first > second == Bazinga!
# # first == second == De novo!
# # second > first == Raj trapaceou!

# time = int(input())
# for i in range(time):
#     a,b = input().split()
#     if a == 'tesoura' and b == 'papel':
#         print(f"Caso #{i+1}: Bazinga!")
#     elif a == 'papel' and b == 'pedra':
#         print(f"Caso #{i+1}: Bazinga!")
#         # 
#     elif a == 'pedra' and b == 'lagartra':
#         print(f"Caso #{i+1}: Bazinga!")
#     elif a == 'lagartra' and b == 'Spock':
#         print(f"Caso #{i+1}: Bazinga!")
#         #
#     elif a == 'Spock' and b == 'tesoura':
#         print(f"Caso #{i+1}: Bazinga!")
#     elif a == 'tesoura' and b == 'lagartra':
#         print(f"Caso #{i+1}: Bazinga!")
#     elif a == 'lagartra' and b == 'papel':
#         print(f"Caso #{i+1}: Bazinga!")
#         #
#     elif a == 'papel' and b == 'Spock':
#         print(f"Caso #{i+1}: Bazinga!")
#     elif a == 'Spock' and b == 'pedra':
#         print(f"Caso #{i+1}: Bazinga!")
#     elif a == 'pedra' and b == 'tesoura':
#         print(f"Caso #{i+1}: Bazinga!")
#     elif a == b:
#         print(f"Caso #{i+1}: De novo!")

#     else:
#         print(f"Caso #{i+1}: Raj trapaceou!")
        



# other


#!/usr/bin/python3
# -*- coding: utf-8 -*-

for i in range(int(input(""))):
    j1, j2 = input("").split()

    if j1 == j2:
        win = "De novo!"
    elif j1 == "pedra":
        if j2 == "tesoura" or j2 == "lagarto":
            win = j1
        else:
            win = j2
    elif j1 == "papel":
        if j2 == "pedra" or j2 == "Spock":
            win = j1
        else:
            win = j2
    elif j1 == "tesoura":
        if j2 == "lagarto" or j2 == "papel":
            win = j1
        else:
            win = j2
    elif j1 == "lagarto":
        if j2 == "Spock" or j2 == "papel":
            win = j1
        else:
            win = j2
    elif j1 == "Spock":
        if j2 == "tesoura" or j2 == "pedra":
            win = j1
        else:
            win = j2

    if win == j1:
        win = "Bazinga!"
    elif win == j2:
        win = "Raj trapaceou!"

    print("Caso #%i:" %(i + 1), win)