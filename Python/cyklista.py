'''
Počas cyklistického tréningu cyklopočítač cyklistu v pravidelných minútových intervaloch meria
nadmorskú výšku (v metroch) a vzdialenosť od posledného merania (v metroch). Záznam môže
vyzerať nasledovne: [[200, 0], [210, 200], [212, 500], [240, 650], [200, 890], [180, 1000], ...] Po
tréningu sa namerané údaje vyhodnotia, aby cyklista vedel, v akej je kondícii. Tréner údaje
vyhodnocuje ručne, pomocou kalkulačky. Tento postup je však zdĺhavý a určite by sa dal
pomocou počítača urýchliť. Vytvorte program, ktorému zadáme namerané údaje a program
vypočíta nasledovné údaje:

 • funkcia vzdialenost() - vráti vzdialenosť v km, ktorú cyklista prešiel,
• funkcia cas() - vráti čas trvania tréningu v minútach,
• funkcia rychlost() - vráti priemernú rýchlosť cyklistu v km/h,
• funkcia najdlhsie_stupanie() - funkcia vráti dĺžku v km najdlhšieho úseku počas
ktorého cyklista stúpal a počet metrov o ktoré vystúpil,
• funkcia najdlhsie_klesanie() - funkcia vráti dĺžku v km najdlhšieho úseku počas
ktorého cyklista klesal a počet metrov o ktoré klesol,
• funkcia stupanie() - funkcia vráti prevýšenie v m, počas ktorého cyklista stúpal,
• funkcia klesanie() - funkcia vráti prevýšenie v m, počas ktorého cyklista klesal,
• funkcia prevýšenie() - funkcia vráti celkové prevýšenie trate v m,
• funkcia najvyssia_rychlost() - funkcia vráti rýchlosť v km/h, ktorú cyklista
dosiahol v najrýchlejšom úseku,
• funkcia najnizsia_rychlost() - funkcia vráti rýchlosť v km/h, ktorú cyklista
dosiahol v najpomalšom úseku,
• funkcia najprudsie_stupanie() - funkcia vráti úsek, v ktorom bolo najprudšie
stúpanie,
• funkcia najprudsie_klesanie() - funkcia vráti úsek, v ktorom bolo najprudšie
klesanie.
'''

progress = [[200, 0], [210, 200], [212, 500], [240, 650], [200, 890], [180, 1000], [170, 1100], [190, 1169], [210, 1181], [230, 1200], [250, 1300], [270, 1400], [290, 1500], [300, 1600], [150, 1700], [140, 1800], [130, 1900], [120, 2000], [110, 2100], [100, 2200]] 
# kazdy novy podzoznam je z nasledujucej minuty predosleho, progress[i][j] i beriem ako os Y, j ako os X   
# progress = [[200, 0], [210, 200], [212, 500], [240, 650], [200, 890], [180, 1000]] 
# #tento list bol zadany na hodine, predlzil som ho pre testovanie funkcii


def get_distance_travelled_per_min(report):
    '''
    :return: vrati list s hodnotami prejdenych vzdialenosti 1-minutoveho useku, index prejdenej vzdialenosti = index minutoveho useku
    '''
    coordsX = [valX[1] for valX in report]
    changesX = [0, ]
    change = 0
    for i in range(len(coordsX)):
        if not coordsX[i] == coordsX[-1]:
            change = coordsX[i+1] - coordsX[i]
            changesX.append(change)
    
    return changesX

def get_list_of_heights(report):
    listOfHeights = []
    for item in report:
        listOfHeights.append(item[0])
    
    return listOfHeights

def get_najdlhsie_stupanie(report):
    '''
    funkcia najdlhsie_stupanie() - funkcia vráti dĺžku v km najdlhšieho úseku počas
    ktorého cyklista stúpal a počet metrov o ktoré vystúpil
    '''

    listOfHeights = get_list_of_heights(report)

    potentialLongestList = []
    longestList = []
    

    # postupne vytvara potentialLongestList, kt. je zaklad pre longestList 
    # ak je potentialLongestList dlhsi ako lognestList, resetuje sa
    
    for i in range(len(listOfHeights)):
        if listOfHeights.index(listOfHeights[i]) != listOfHeights.index(listOfHeights[-1]): # ak nie je poslende
            if listOfHeights.index(listOfHeights[i]) == 0 or listOfHeights[i] > listOfHeights[i-1]: #ak je prve alebo vacsie ako predosle
                potentialLongestList.append(listOfHeights[i]) 
                if len(potentialLongestList) > len(longestList): #ak ma potenialLongestList viac prvkov nez longestList 
                    longestList = potentialLongestList #narodi sa novy longestList, stary zdochne :( (chudacik)

            elif listOfHeights[i] < listOfHeights[i-1]: #ak nevysiel dalej, potentialLongestList sa resetuje
                potentialLongestList = []
    
    longestListStart = listOfHeights.index(longestList[0])
    longestListEnd = listOfHeights.index(longestList[-1])

    fullLongestList = []
    for i in range(len(longestList)):
        fullLongestList.append(report[longestListStart:longestListEnd + 1])

    distanceTravelled = [section[1] for section in fullLongestList]

    ascendedBy = sum(longestList) - longestList[0]

    return(ascendedBy, distanceTravelled)    

def get_najdlhsie_klesanie(report):
    '''
    funkcia najdlhsie_klesanie() - funkcia vráti dĺžku v km najdlhšieho úseku počas
    ktorého cyklista klesal a počet metrov o ktoré klesol
    '''
    listOfHeights = get_list_of_heights(report)

    potentialLongestList = []
    longestList = []
    

    # funkcia get_najdlhsie_stupanie(), iba s opacnymi znamienkami
    
    for i in range(len(listOfHeights)):
        if listOfHeights.index(listOfHeights[i]) != listOfHeights.index(listOfHeights[-1]): # ak nie je poslende
            if listOfHeights.index(listOfHeights[i]) == 0 or listOfHeights[i] < listOfHeights[i-1]: #ak je prve alebo vacsie ako predosle
                potentialLongestList.append(listOfHeights[i]) 
                if len(potentialLongestList) > len(longestList): #ak ma potenialLongestList viac prvkov nez longestList 
                    longestList = potentialLongestList #narodi sa novy longestList, stary zdochne :( (chudacik)

            elif listOfHeights[i] > listOfHeights[i-1]: #ak nevysiel dalej, potentialLongestList sa resetuje
                potentialLongestList = []

    longestListStart = listOfHeights.index(longestList[0])
    longestListEnd = listOfHeights.index(longestList[-1])

    fullLongestList = []
    for i in range(len(longestList)):
        fullLongestList.append(report[longestListStart:longestListEnd + 1])

    distanceTravelled = [section[1] for section in fullLongestList]

    ascendedBy = sum(longestList) - longestList[0]

    return(ascendedBy, distanceTravelled) 
    
def get_najvyssia_rychlost(speeds):
    '''
    I funkcia najvyssia_rychlost() - funkcia vráti rýchlosť v km/h, ktorú cyklista
    dosiahol v najrýchlejšom úseku
    '''
    #podla funkc. get_distance_travelled_per_min(report) s tymto listom 3. miesto - index 2
    #   [0, 200, 300, 150, 240, 110, 100, 69, 12, 19, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    fastest = max(speeds)
    fastestInKMH = (fastest/1000)*60

    return fastestInKMH

def get_najnizsia_rychlost(speeds):
    '''
    J funkcia najnizsia_rychlost() - funkcia vráti rýchlosť v km/h, ktorú cyklista
    dosiahol v najpomalšom úseku
    '''
    #podla funkc. get_distance_travelled_per_min(report) s tymto listom 3. miesto - index 2
    #   [0, 200, 300, 150, 240, 110, 100, 69, 12, 19, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    speeds = speeds[1:]
    slowest = min(speeds)
    slowestInKMH = (slowest/1000)*60

    return slowestInKMH

def get_height_increase_per_min(report):
    '''
    recyklovana verzia funkcie get_distance_travelled_per_min()
    '''
    coordsX = [valX[0] for valX in report] #recyklacia nastava tu, tipnite si kde :D
    changesX = [0, ]
    change = 0
    for i in range(len(coordsX)):
        if not coordsX[i] == coordsX[-1]:
            change = coordsX[i+1] - coordsX[i]
            changesX.append(change)
    
    return changesX

def get_najprudsie_stupanie(heights, report): 
    '''
    K funkcia najprudsie_stupanie() - funkcia vráti úsek, v ktorom bolo najprudšie
    stúpanie

    recyklovana verzia funkcie get_najvyssia_rychlost() :)
    '''
    highest = max(heights)
    highestIndex = report.index(report[heights.index(highest)])

    return highestIndex

def get_najprudsie_klesanie(heights, report): 
    '''
    L funkcia najprudsie_klesanie() - funkcia vráti úsek, v ktorom bolo najprudšie
    klesanie

    recyklovana verzia funkcie get_najprudsie_stupanie()
    '''
    lowest = min(heights)
    lowestIndex = report.index(report[heights.index(lowest)])

    return lowestIndex

def get_cyclist_info(report):
    '''
    A unkcia vzdialenost() - vráti vzdialenosť v km, ktorú cyklista prešiel,
    B funkcia cas() - vráti čas trvania tréningu v minútach,
    C funkcia rychlost() - vráti priemernú rýchlosť cyklistu v km/h,
    D funkcia najdlhsie_stupanie() - funkcia vráti dĺžku v km najdlhšieho úseku počas
    ktorého cyklista stúpal a počet metrov o ktoré vystúpil,
    E funkcia najdlhsie_klesanie() - funkcia vráti dĺžku v km najdlhšieho úseku počas
    ktorého cyklista klesal a počet metrov o ktoré klesol,
    F funkcia stupanie() - funkcia vráti prevýšenie v m, počas ktorého cyklista stúpal,
    G funkcia klesanie() - funkcia vráti prevýšenie v m, počas ktorého cyklista klesal,
    H funkcia prevýšenie() - funkcia vráti celkové prevýšenie trate v m,
    I funkcia najvyssia_rychlost() - funkcia vráti rýchlosť v km/h, ktorú cyklista
    dosiahol v najrýchlejšom úseku,
    J funkcia najnizsia_rychlost() - funkcia vráti rýchlosť v km/h, ktorú cyklista
    dosiahol v najpomalšom úseku,
    K funkcia najprudsie_stupanie() - funkcia vráti úsek, v ktorom bolo najprudšie
    stúpanie,
    L funkcia najprudsie_klesanie() - funkcia vráti úsek, v ktorom bolo najprudšie
    klesanie.
    '''
    vzdialenost = get_distance_travelled_per_min(report)
    vzdialenostKM = sum(vzdialenost)/1000 #spolu vzdialenost (premenena z m na km), A

    vysky = get_height_increase_per_min(progress)

    cas = len(report) - 1 #1. hodnota povazovana za zaciatok, kde sa zacina merat cas, cize sa nepocita, v minutach, B

    avgRychlost = vzdialenostKM * 60 #premena na km/h, C

    stupanie = get_najdlhsie_stupanie(report) # D+E zaklad
    dlzkaStupania = len(stupanie[1]) # D1
    najdlhsieStupanie = stupanie[0] # F + D2

    klesanie = get_najdlhsie_klesanie(report)
    dlzkaKlesania = len(klesanie[1]) # E1
    najdlhsieKlesanie = klesanie[0] # G + E2

    finalElevationDiff = report[-1][0] - report[0][0] #H

    topRychlost = get_najvyssia_rychlost(vzdialenost) # I

    minRychlost = get_najnizsia_rychlost(vzdialenost) # J

    najprudsieStupanie = get_najprudsie_stupanie(vysky, report) # K

    najprudsieKlesanie = get_najprudsie_klesanie(vysky, report) # L

    return(f"Vzdialenost prejdena: {vzdialenostKM} km, \n{cas} minut celkovo, \n{avgRychlost} km/h priemerna rychlost, \n{dlzkaStupania} min najdlhsieho stupania, \n{najdlhsieStupanie} m najdlhsieho stupania, \n{dlzkaKlesania} min najdlhsieho klesania, \n{najdlhsieKlesanie} m najdlhsieho klesania, \n{finalElevationDiff} konecne prevysenie, \n{topRychlost} km/h bola najvyssia dosiahnuta rychlost, \n{minRychlost} km/h bola nanizsia dosiahnuta rychlost, \nNajprudsie stupanie nastalo na useku c. {najprudsieStupanie}, \nNajprudsie stupanie nastalo na useku c. {najprudsieKlesanie}")
    

pisanie = get_cyclist_info(progress)

cyklista_output = "cyklista_output.txt"

with open(cyklista_output, "w") as text:
    text.write(pisanie)
    text.write(f"\n\n\nVstup bola neznama 'progress': {progress}")
    text.close