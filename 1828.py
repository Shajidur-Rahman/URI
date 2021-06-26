# pedra = rock
# papel =  paper
# tesoura =  scissors
# lagart =  lizard
# Spock = Spock

# first > second == Bazinga!
# first == second == De novo!
# second > first == Raj trapaceou!

time = int(input())
for i in range(time):
    a,b = input().split()
    if a == 'tesoura' and b == 'papel':
        print(f"Caso #{i}: Bazinga!")
    elif a == 'papel' and b == 'pedra':
        print("Bazinga!")
        # 
    elif a == 'pedra' and b == 'lagartra':
        print("Bazinga!")
        #
    elif a == 'Spock' and b == 'tesoura':
        print("Bazinga!")
    elif a == 'tesoura' and b == 'lagartra':
        print("Bazinga!")
    elif a == 'lagartra' and b == 'papel':
        print("Bazinga!")
        #
    elif a == 'papel' and b == 'Spock':
        print("Bazinga!")
    elif a == 'Spock' and b == 'pedra':
        print("Bazinga!")
    elif a == 'pedra' and b == 'tesoura':
        print("Bazinga!")
    elif a == b:
        print("De novo!")

    else:
        print("Raj trapaceou!")
        