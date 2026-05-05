from queue import Queue
from copy import deepcopy

original_mapa = [[znak for znak in riadok] for riadok in '''
..o..#.f
v.......
.#......
........
........
.o......
'''.split()]

veterinar_mapa = deepcopy(original_mapa)
slintacka_mapa = deepcopy(original_mapa)
velkost_riadku, velkost_stlpca = len(slintacka_mapa), len(slintacka_mapa[0])
rV, sV = 1,0
rO1, sO1 = 0,2
rO2, sO2 = 5,1

slintacka = Queue()
slintacka.put((rO1, sO1))
slintacka.put((rO2, sO2))

veterinar = Queue()
veterinar.put((rV, sV))

smery = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def je_dobre_policko_slintacka(policko:tuple[int]):
    if 0 <= policko[0] < velkost_riadku and 0 <= policko[1] < velkost_stlpca:
        znak = slintacka_mapa[policko[0]][policko[1]]
        if znak == '.' or znak == 'f':
            return True
    
    return False

def simuluj_slintacku():
    while not slintacka.empty():
        policko = slintacka.get()
        stara_hodnota = slintacka_mapa[policko[0]][policko[1]]
        for smer in smery:
            nove_policko = (policko[0] + smer[0], policko[1] + smer[1])
            if je_dobre_policko_slintacka(nove_policko):
                slintacka.put(nove_policko)
                slintacka_mapa[nove_policko[0]][nove_policko[1]] = stara_hodnota + 2 if stara_hodnota != 'o' else 2

def je_dobre_policko_veterinar(nove_policko:tuple[int], stare_policko:tuple[int]):
    if 0 <= nove_policko[0] < velkost_riadku and 0 <= nove_policko[1] < velkost_stlpca:
        hodnota_slintacky = slintacka_mapa[nove_policko[0]][nove_policko[1]]
        if veterinar_mapa[nove_policko[0]][nove_policko[1]] == '.' or veterinar_mapa[nove_policko[0]][nove_policko[1]] == 'f':
            hodnota_veterinara = veterinar_mapa[stare_policko[0]][stare_policko[1]]
            if hodnota_veterinara == 'v':
                return True
            if hodnota_veterinara + 1 < hodnota_slintacky:
                return True
        
    
    return False

def simuluj_veterinara():
    while not veterinar.empty():
        policko = veterinar.get()
        stara_hodnota = veterinar_mapa[policko[0]][policko[1]]
        for smer in smery:
            nove_policko = (policko[0] + smer[0], policko[1] + smer[1])
            if je_dobre_policko_veterinar(nove_policko, policko):
                veterinar.put(nove_policko)
                veterinar_mapa[nove_policko[0]][nove_policko[1]] = stara_hodnota + 1 if stara_hodnota != 'v' else 1

simuluj_slintacku()

for riadok in slintacka_mapa:
    for hodnota in riadok:
        print(f'{hodnota:>3}', end=" ")
    print()

print('-----------------')

simuluj_veterinara()

for riadok in veterinar_mapa:
    for hodnota in riadok:
        print(f'{hodnota:>3}', end=" ")
    print()

print()