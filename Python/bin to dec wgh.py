def is_number(vstup):
    try:
        int(vstup)
        return True
    except ValueError:
        return False

def bin_to_dec(vstup):
    if is_number(vstup):
        podiel = int(vstup)
    else:
        raise ValueError("Viem pracovať len s prirodzenými číslami!")
    
    if podiel < 0:
        raise ValueError("Neberiem mínusové čísla!")
    elif podiel == 0:
        return 0
    elif podiel > 0:
        zvysok = 0
        cislo2 = ""

        while podiel > 0:
            zvysok = podiel % 2
            cislo2 += str(zvysok)
            podiel = int(podiel/2)
        cislo2 = cislo2[::-1]
        return cislo2

while True:
    try:
        vstup = input("Zadaj ľubovoľné prirodzené číslo na premenu: ")
        premenene = bin_to_dec(vstup)
        print(f"Číslo {vstup} sa v dvojkovej sustave zapisuje ako {premenene}")
        break
    except ValueError as oops:
        print(oops)



