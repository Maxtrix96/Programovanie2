import random

def play_game(userNumber, numberOfGuesses=0):
    number = random.randint(100, 201)
    result = ""
    previousGuesses = []
    while True:
        if userNumber not in range(100, 201):
            print("Incorrect input. Guess must be between 100 and 200.")
            previousGuesses.append(userNumber)
            userNumber = int(input("Enter a new number: "))
            numberOfGuesses += 1
        elif userNumber == number:
            numberOfGuesses += 1
            previousGuesses.append(userNumber)
            result = f"You gussed the number! ({number})\nYour guesses: {previousGuesses}\nYou used {numberOfGuesses} guesses."
            print(result)
            break
        elif userNumber > number:
            result = "My number is smaller."
            previousGuesses.append(userNumber)
            print(result)
            userNumber = int(input("Guess a new number: "))
            numberOfGuesses += 1
        elif userNumber < number:
            result = "My number is larger."
            previousGuesses.append(userNumber)
            print(result)
            userNumber = int(input("Guess a new number: "))
            numberOfGuesses += 1

userGuess = int(input("Enter your first guess: "))
play_game(userGuess)