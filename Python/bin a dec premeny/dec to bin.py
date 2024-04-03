def dec_to_bin(num, base):
    if not num.isdigit():
        raise ValueError("Beriem len číselný vstup!")
    
    num = int(num)
    result = ""
    while num > 0:
        remainder = num % base
        num = num // base
        result += f"{remainder}"

    return result[::-1]

try:
    user_input = input("Zadaj kladné číslo v desiatkovej sústave: ")
    print(dec_to_bin(user_input, 2))
except ValueError as err:
    print(err)