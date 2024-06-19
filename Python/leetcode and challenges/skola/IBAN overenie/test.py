IBAN = "SK6981800000000009876543"
BBAN = IBAN[4:24]


def modulo_11(BBAN):
    weights = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6] # váhy
    pref = list(map(int, BBAN[4:10]))[::-1] # ktoré cisla skontrolovat
    account_num = list(map(int, BBAN[10:20]))[::-1]
    multiplied = []
    for i in range(len(weights)):
        if i <= 5:
            multiplied.append(weights[i] * pref[i])
        multiplied.append(weights[i]*account_num[i])
    

    total = sum(multiplied)
    valid = total % 11 == 0
    return valid

def mod_97(IBAN):
    test_IBAN = IBAN[4:] + IBAN[:4]
    print(test_IBAN)

mod_97(IBAN)