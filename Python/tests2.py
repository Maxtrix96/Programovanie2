import random

def test1():
    def counter(numbers):
        counter = {}
        for num in numbers:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        print("a")
        return counter
    
    num_input = input("Enter any amount of numbers you'd like, make sure to separate them with spaces: ").split()
    num_list = [int(num) for num in num_input]
    result = counter(num_list)
    print(result)

def test2():
    #Write a function that takes a string as input and returns a dictionary that maps each unique word in the string to the number of times it appears.
    user_input = input("Write any words and I'll count how many times each words appears in your input: ").split()
    input_dict = {}
    for word in user_input:
        if word in input_dict:
            input_dict[word] += 1
        elif word not in input_dict:
            input_dict[word] = 1
    print(input_dict)

def test3():
    #Write a function that takes two lists of numbers as input and returns a new list that contains only the unique numbers that appear in both input lists.
    user_input_1 = input("Write the first list of numbers, separated by whitespaces: ")
    numbers_list_1 = user_input_1.split()
    numbers_1 = [int(num) for num in numbers_list_1]
    numbers_1_set = set(numbers_1)

    user_input_2 = input("Write the second list of numbers, separated by whitespaces: ")
    numbers_list_2 = user_input_2.split()
    numbers_2 = [int(num) for num in numbers_list_2]
    numbers_2_set = set(numbers_2)

    numbers_all = numbers_1 + numbers_2
    numbers_set = set(numbers_all)
    common_numbers = numbers_1_set.intersection(numbers_2_set)
    print(f"The unique numbers of your two inputted number lists are: {numbers_set}")
    print(f"The common numbers of your two inputted number lists are: {common_numbers}")

def what():
    for i in range(0, 24):
        print(i+1)

def count_words(text):
    print(len((text).split(" ")))

def test4():
    numbers_list = [1, 1, 2, 2, 3, 4, 7, 8, 7, 9, 2, 1, 3, 15]
    numbers_list_2 = [1, 5, 8, 9, 1, 2, 4, 12, 15, 17, 1]
    numbers_set = set(numbers_list)
    numbers_set_2 = set(numbers_list_2)
    unique_numbers = numbers_set.intersection(numbers_set_2)
    print(unique_numbers)




