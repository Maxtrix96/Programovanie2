# greedy

bankovky = [500, 200, 100, 50, 20, 10, 5, 2, 1]

def kolko_bankoviek(chcenaSuma):
    vysledok:dict = {}

    for bankovka in bankovky:
        vysledok[bankovka] = chcenaSuma // bankovka
        chcenaSuma = chcenaSuma % bankovka
    
    return vysledok

print(kolko_bankoviek(1234599))