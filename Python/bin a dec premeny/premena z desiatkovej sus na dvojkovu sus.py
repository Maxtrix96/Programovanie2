def je_cislo(vstup):
    try:
        int(vstup)
        return True
    except ValueError:
        return False

def premena_10_na_2(vstup):
    if not je_cislo(vstup):
        raise ValueError("Nebol zadaný číselny vstup.")
    podiel = int(vstup)

    if podiel == 0:
        return 0
    elif podiel < 0:
        raise ValueError("Neprijimam minusove hodnoty")

    str_cislo2 = ""

    while podiel > 0:
        zvysok = podiel%2
        podiel = podiel//2
        str_cislo2 = str_cislo2 + str(zvysok)
    cislov2 = str_cislo2[::-1]
    return cislov2

while True:
    try:
        vstup = input("Zadaj cislo v desiatkovej sustave: ")
        cislo_v2 = premena_10_na_2(vstup)
        print(f"Číslo {vstup} sa v dvojkovej sustave zapisuje ako {cislo_v2}")
        break 
    except ValueError as chyba:
        print(chyba)