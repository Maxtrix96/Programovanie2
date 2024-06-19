pomocka  = "SK  69  8180 000000 0009876543"
pomocka  = "SK  62  8180 000000 0098765432"
#           01  23  4567 890123 4567890123
#           00  00  0000 001111 1111112222
#                  |pred|cislie|c.uctu

test_IBAN = "SK6981800000000009876543"
def kontrola_IBAN(IBAN:str):
    must_be_SK = False # nastavte podla potreby, ak True -> prve dve pismena musia byt SK, inak vrat nie

    if must_be_SK:
        if not IBAN[0:2] == "SK":
            return "nie"
        
    if not len(IBAN) <= 34: # ak je iban prilis dlhy, vrat nie
        return "nie"
    
    valid_bank:list = ['0200', '0900', '0720', '1100', '1111', '3000', '3100', '5200', '5600', '5900', '6500', '7300', '7500', '7930', '8050', '8100', '8120', '8130', '8170', '8160', '8180', '8191', '8400', '8320', '8330', '8350', '8360', '8370', '8390', '8410', '8420', '8430', '9950', '9951', '9952', '2010']
    # platne kody bank zo zadania
    BBAN:str = IBAN[4:24] # kod banky + 6-cif. predcislie + 10-cif. cislo uctu
    
    def mod_97(IBAN:str):
        alphabet:dict = {key:value for value, key in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
        test_IBAN:list = [i for i in IBAN[4:] + IBAN[:4]]
        for index, char in enumerate(test_IBAN):
            if char.isalpha():
                test_IBAN[index] = 10 + alphabet[char] # nahrad kazde pismeno za spravne cislo podla miesta v abecede
            elif char.isdigit():
                test_IBAN[index] = int(char) # ak nie si cislo, premen na integer, aby nebolo treba map()
            else:
                return False # ak znak nie je ani pismeno ani cislo, vrat False (nemalo by treba ak funguje spravne)
        adjusted_IBAN:int = int("".join(list(map(str, test_IBAN))))
        valid_IBAN:bool = adjusted_IBAN % 97 == 1

        return True if valid_IBAN else False

    def modulo_11(BBAN:str):
        weights:list = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6] # váhy
        pref:list = list(map(int, BBAN[4:10]))[::-1] # 6-cif. predcislie 1 2 3 4 5 6 | 6 5 4 3 2 1
        account_num = list(map(int, BBAN[10:20]))[::-1] # 10-cif. cislo uctu
        products:list = [] 
        for i in range(len(weights)):
            if i <= 5:
                products.append(weights[i] * pref[i])
            products.append(weights[i] * account_num[i])

        valid:bool = sum(products) % 11 == 0
        return valid
    
    is_alnum = IBAN.isalnum()
    is_alpha = IBAN[0:2].isalpha()
    is_digit = IBAN[2:4].isdigit()
    is_valid_bank = BBAN[0:4] in valid_bank
    passed_modulo_11 = modulo_11(BBAN)
    passed_mod_97 = mod_97(IBAN)
    #print(f"{is_alnum= } {is_alpha= } {is_digit= } {is_valid_bank= } {passed_modulo_11= } {passed_mod_97= }")

    if is_alnum and is_alpha and is_digit and is_valid_bank and passed_modulo_11 and passed_mod_97:
        return "ano"
    else:
        return "nie"
    
#result = kontrola_IBAN(test_IBAN)
#print(result)

def accept_input():
    amount = int(input())
    codes_to_test = []

    if 1 <= amount <= 1_000: # kontrola mnozstva cisiel IBAN na kontrolu
        for _ in range(amount):
            code = input()
            codes_to_test.append(code)
    
    for IBAN in codes_to_test:
        kontrola_IBAN(IBAN)

accept_input() # pre system PALMA STROM

"""def test_provided_codes():
    codes = ["SK6981800000000009876543", "SK6781800000000009876543", "SK6281800000000098765432"]
    #codes = ["SK6281800000000098765432"]
    for code in codes:
        print(kontrola_IBAN(code))

test_provided_codes()"""