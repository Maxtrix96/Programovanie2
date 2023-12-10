
def je_cislo(vstup:str):
    try:
        int(vstup)
        return True
    except ValueError:
        return False

def is_binary(str_num:str):
    invalidDigits = "23456789"
    for letter in str_num:
        if letter in invalidDigits:
            return False
    return True

def convert_bin_to_dec(str_number: str):
    '''
    :param str_number: takes a number as a string
    '''

    if not je_cislo(str_number):
        raise ValueError("Nebol zadaný číselny vstup.")

    if str_number == "0":
        return "0"
    elif int(str_number) < 0:
        raise ValueError("Nebol zadany vstup v dvojkovej sustave!")
    elif not is_binary(str_number):
        raise ValueError("Nebol zadany vstup v dvojkovej sustave!")
    
    numberListTemp = list(map(int, [letter for letter in str_number]))[::-1]
    numberListFinal = []
    for i in range(len(numberListTemp)):
        numberListFinal.append(2**i * numberListTemp[i])
    return sum(numberListFinal)


while True:
    try:
        userInput = input("Zadaj cislo ktore chces premenit z 2 sús. na 10 sús.: ")
        print(convert_bin_to_dec(userInput))
        break 
    except ValueError as chyba:
        print(chyba)

