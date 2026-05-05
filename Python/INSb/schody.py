prvyRiadok = [int(val) for val in input().split(" ")]
maxVyska = prvyRiadok[1]

schody = [int(val) for val in input().split(" ")]

global postupnost
postupnost:list = [0]
najdenePostupnosti:list = []


def kracaj(odIdx): # leniva hruba sila
    if odIdx == len(schody): # baza
        najdenePostupnosti.append(postupnost.copy())
        return

    for i in range(len(schody), odIdx, -1): # rob co najvacsie kroky
        if sum(schody[odIdx:i]) <= maxVyska:
            postupnost.append(i)
            kracaj(i)
            postupnost.pop() # po rekurzii vymaz uz vyhladanu postupnost


najdeneRieseniaVolani = [[]] * (prvyRiadok[0] - 1) + [[4]] # pole pre uz vypocitane volania funkcie

def kracajDP(odIdx):
    if najdeneRieseniaVolani[odIdx] is not None:
        
        return najdeneRieseniaVolani[odIdx]
    
    podPostupnost = []
    for i in range(len(schody), odIdx, -1): # rob co najvacsie kroky
        if sum(schody[odIdx:i]) <= maxVyska:
            podPostupnost.append(i)
            podPostupnost += kracajDP(i) 
            najdeneRieseniaVolani[i].append(podPostupnost)
            podPostupnost.clear()

# nestiham pre zapocty:
# staci vediet, kolko rieseni, teda na danom indexe si zapamataj pocet moznych dalsich krokov
# rob odzadu, rekurzivne 

kracaj(0)

print(najdenePostupnosti)