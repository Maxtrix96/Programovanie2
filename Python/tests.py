def test1():
    name = input("What's your fisrt name? ")
    print(f"Hello, {name}")

def test2():
    length = int(input("What's the length? "))
    width= int(input("What's the width? "))
    area = length * width
    print(area)

def test3():
    # Take input from user
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("The number is even!")
    elif number % 2 != 0:
        print("The number is odd!")

def test4():
    # Take input from user as a list of integers
    num_list = input("Enter a list of integers separated by spaces: ").split()
    num_list = [int(num) for num in num_list]

    # Create a new list with only even numbers
    even_list = [num for num in num_list if num % 2 == 0]

    # Print the new list
    print("The even numbers in the list are:", even_list)

def test5():
    import random

    # Take input from user
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    # Generate random choice for computer
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Determine winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif user_choice == "rock":
        if computer_choice == "scissors":
            result = "You win!"
        else:
            result = "Computer wins!"
    elif user_choice == "paper":
        if computer_choice == "rock":
            result = "You win!"
        else:
            result = "Computer wins!"
    else:
        if computer_choice == "paper":
            result = "You win!"
        else:
            result = "Computer wins!"

    # Output result
    print("You chose", user_choice, "and the computer chose", computer_choice + ".")
    print(result)

# String reversal

def test6():
    string = input("Enter a string: ")
    reversed_string = string[::-1]
    print("The reversed string is:", reversed_string)

def test7():
    num_list = input("Select numbers separated by a whitespace: ").split()
    num_list = [int(num) for num in num_list]
    even_sum = 0
    for num in num_list:
        if num % 2 == 0:
            even_sum += num
    print("The sum of even numbers in the list is:", even_sum)

# Write a Python program to find the largest number in a list of numbers. The program should take input from the user (a list of numbers separated by commas), 
# and output the largest number in the list.

def test8():
    num_list = input("Enter a list of numbers separated by commas: ").split(",")
    num_list = [int(num) for num in num_list]
    print(max(num_list))

# Write a Python program to count the number of vowels in a string. The program should take input from the user (a string), 
# and output the number of vowels in the string.
def test9():
    def count_vowels(string):
        vowels = "aeiouAEIOU"
        count = 0

        for letter in string: 
            if letter in vowels:
                count += 1

        return count
    string = input("Write any sentence you'd like! ")
    num_vowels = count_vowels(string)
    print("Number of vowels in your sentence: ", num_vowels)

# Write a Python program that takes a string input from the user and returns the reverse of the string.
def test10():
    string = input("Enter a string: ")
    reversed_string = string[::-1]
    print(reversed_string)

# Write a Python program that takes a list of numbers as input from the user and returns a new list with only
# the unique numbers from the original list (i.e., no duplicates). 
def test11():
    def unique_list(lst):
        unique_lst = (list(set(lst)))
        unique_lst.sort()
        result = unique_lst[1]
        print(unique_lst)
        return result
    
    num_list = input("Enter a list of numbers, make sure to separate with spaces. ").split()
    num_list = [int(num) for num in num_list]

    unique_nums = unique_list(num_list)
    print(unique_nums)


# Write a Python program that asks the user for their name and age, 
# and then prints out a message telling them how old they will be in 10 years.
def test_12():
    name_age = input("Tell us your name and age, separated by a comma: ").split(",")
    age = int(name_age[1]) + 10
    print(age)

# Write a Python program that takes a list of integers as input and returns a new list containing only the 
# even numbers from the original list.
def test13():
    number_list = input("Enter as many numbers as you want, separated by spaces: ").split()
    number_list = [int(num) for num in number_list]
    even_list = [num for num in number_list if num % 2 == 0]
    print(even_list)

def letter_position(letter):
    letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    alphabet = letters.split()
    letter_position = alphabet.index(letter) + 1
    print(letter_position)

def letter_check(word):
    valid_words = []
    if word[0] == word[-1]:
        valid_words.append(word)
        print(True)
        return(True, valid_words)
    else:
        print(False)
        return(True, valid_words)


def yes_no_decider(option_1, option_2):
    import random
    choices = [option_1, option_2]
    print(random.choice(choices))



def find_index(choices, target):
    sorted_choices = sorted(choices)  # Use the sorted() function to create a sorted list
    print(type(sorted_choices))
    indexes = len(sorted_choices)
    low = 0
    high = indexes - 1
    mid = (low + high) // 2  # Use integer division (//) to find the middle index

    while low <= high:  # Use a proper loop condition for binary search
        if sorted_choices[mid] == target:
            print("Found it! The value is at index ", mid)
            return mid
        elif sorted_choices[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    
    print("Value not found in the list")
    return -1

def find_index_initiliaze():
    index = find_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 18, 17, 19, 17, 19, 18], 5)
    if index != -1:
        print("Value found at index: ", index)
    else:
        print("Value not found in the list")

for i in range(70):
    print(i)