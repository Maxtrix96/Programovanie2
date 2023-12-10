maximum = 91
minimum = 24
outlier = False
number = 0
end_task = "amogus"
while True:
    if True:
        number = int(input("Set the variable number: "))
        if number > maximum or number < minimum:
            outlier = True
            print(F"Your number ({number}) is an outlier!")
            print("Please type end if you want to finish the program.", end="")
            end_task = str(input("Would you like to finish?"))
        elif number >= minimum and number <= maximum:
            outlier = False
            print(F"Your number ({number}) isn't an outlier!")
            print("Please type end if you want to finish the program.", end="")
            end_task = str(input("Would you like to finish?"))
        if end_task == "end":
            break
    