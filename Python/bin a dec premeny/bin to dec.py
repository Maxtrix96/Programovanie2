def bin_to_dec(num:str) -> int:
    if not num.isdigit():
        raise ValueError("Nebol zadaný číselný vstup!")
    elif {"2", "3", "4", "5", "6", "7", "8", "9"}.intersection(set(num)):
        raise ValueError("Nebol zadaný vstup v dvojkovej sústave!")
    
    powers = list(range(len(num)))[::-1]
    result = []

    for i in powers:
        result.append(2**powers[i] * int(num[i]))

    return sum(result)

"""try:
    user_input = input("Zadaj kladné číslo v dvojkovej sústave: ")
    print(bin_to_dec(user_input))
except ValueError as err:
    print(err)"""

print(bin_to_dec("010"))