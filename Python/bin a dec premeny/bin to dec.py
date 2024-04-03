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

array = [1, 2, 4, 9, 1]

are_all_int = all(isinstance(x, int) for x in array)

print(are_all_int)