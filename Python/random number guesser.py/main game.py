import random

def play_game(MIN_NUM, MAX_NUM):
    number = random.randint(MIN_NUM,MAX_NUM)
    low, high = MIN_NUM, MAX_NUM
    guesses = 0
    list_of_guesses = []

    while True:
        my_choice = (low+high)//2
        list_of_guesses.append(my_choice)
        guesses += 1

        if my_choice == number:
            game_report = f"You won! The number was: {number}.\nIt took you {guesses} guesses.\nYour guesses were: {list_of_guesses}."
            print(game_report)
            break
        elif my_choice > number:
            print(f"Guessed number: {my_choice}. Mine is smaller!")
            high = my_choice - 1
            my_choice = (low+high)//2
        elif my_choice < number:
            print(f"Guessed number: {my_choice}. Mine is larger!")
            low = my_choice + 1
            my_choice = (low+high)//2
        
play_game(100, 201)