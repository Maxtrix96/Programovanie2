import random

def play_game(userNumber, numberOfGuesses=0):
    number = random.randint(100, 201)
    result = ""
    previousGuesses = []
    while True:
        if userNumber not in range(100, 201):
            print("Nezadal si spravne cislo!")
            previousGuesses.append(userNumber)
            userNumber = int(input("Zadaj nove cislo: "))
            numberOfGuesses += 1
        elif userNumber == number:
            numberOfGuesses += 1
            previousGuesses.append(userNumber)
            result = f"Nasiel si cislo! Cislo bolo: {number}\nTvoje cisla: {previousGuesses}\nNa uhadnutie si potreboval {numberOfGuesses} uhadnuti."
            print(result)
            break
        elif userNumber > number:
            result = "Moje cislo je mensie!"
            previousGuesses.append(userNumber)
            print(result)
            userNumber = int(input("Zadaj nove cislo: "))
            numberOfGuesses += 1
        elif userNumber < number:
            result = "Moje cislo je vacsie!"
            previousGuesses.append(userNumber)
            print(result)
            userNumber = int(input("Zadaj nove cislo: "))
            numberOfGuesses += 1

userGuess = int(input("Zadaj cislo: "))
play_game(userGuess)