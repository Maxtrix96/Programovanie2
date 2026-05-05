k = 5 # dlzka kodu
kod = [0]*k
rozsah = 5 # ktore cislice od 1 mame k dispozicii
pocet = 0

def increment():
    global pocet
    pocet += 1

def generuj(uroven):

    if uroven == k: 
        print(kod)
        return

    for cislica in range(0, rozsah + 1):
        kod[uroven] = cislica
        generuj(uroven + 1)

def generuj_iba_parne(uroven):

    if uroven == k: 
        print(kod)
        return

    for cislica in range(0, rozsah + 1, 2):
        kod[uroven] = cislica
        generuj_iba_parne(uroven + 1)

def je_bez_opakovania(kod):
    for i in range(len(kod)):
        for j in range(i+1, len(kod)):
            if kod[i] == kod[j]:
                return False

    return True

def generuj_bez_vypisania_opakovanych(uroven):
    if uroven == k: 
        if je_bez_opakovania(kod):
            print(kod)
        return

    for cislica in range(0, rozsah + 1):
        kod[uroven] = cislica
        generuj_bez_vypisania_opakovanych(uroven + 1)

def generuj_bez_opakovania(uroven):
    if uroven == k:
        print(kod)
        return

    for cislica in range(1, rozsah + 1):
        if not (cislica in kod[0:uroven]): # preskoc hodnoty ktore tam uz su
            kod[uroven] = cislica
            generuj_bez_opakovania(uroven + 1)

vyuzite:list[bool] = [False] * (rozsah + 1)

def generuj_bez_opakovania_lepsie(uroven):
    if uroven == k:
        print(kod)
        vyuzite[kod[-1]] = False
        increment()
        return

    for cislica in range(1, rozsah + 1):
        if not (vyuzite[cislica]): 
            kod[uroven] = cislica
            vyuzite[cislica] = True
            generuj_bez_opakovania_lepsie(uroven + 1)
            vyuzite[cislica] = False

generuj_bez_opakovania_lepsie(0)

print(pocet)

class test:
    def __init__(self, co):
        self.co = co
    
    def vypis(self):
        print(self.co)

testiky = test("a")

testiky.vypis()