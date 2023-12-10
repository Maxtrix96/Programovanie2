userInput = int(input("Zadaj pocet penazi na rozklad: "))
optionsInput = [500, 200, 100, 50, 20, 10, 5, 2, 1]

def break_down_money(amount: int, optionsList):
    options = {amt: 0 for amt in optionsList}
    for amt in options:
        options[amt] = amount // amt
        amount %= amt

    return options

print(break_down_money(userInput, optionsInput))

