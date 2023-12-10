#kolko prsiel blokov
#zitsi najkratsiu cestu (2. program)
#spravnost (ci ide len SJVZ)

strany = "SJVZ"
vstup = "SVJ"
position = [0, 0]

movementsX = ["V", "Z"]
movementsY = ["S", "J"]

def is_valid(movements):
    for i in range(len(movements)):
        if movements[i] not in strany:
            return False
    return True

def axis_X(movements): #pohyb po osi X
    movement = 0
    for move in movements:
        if move in movementsX:
            if move == "V":
                movement += 1
            elif move == "Z":
                movement -= 1
    return movement

def axis_Y(movements): #pohyb po osi Y
    movement = 0
    for move in movements:
        if move in movementsY:
            if move == "S":
                movement += 1
            elif move == "J":
                movement -= 1
    return movement

def movements_count(movements): #pocet pohnuti
    movementsCount = len(movements)
    return movementsCount

def new_position(movements): #kde skonci
    position = [0, 0]
    position[0] = axis_X(movements)
    position[1] = axis_Y(movements)
    return position

def minimum_movements(movements): #kolko min. pohnuti na to, aby sa dostal tam kde je zo startu
    minimumMovements = abs(axis_X(movements)) + abs(axis_Y(movements))
    return f"Minimalny pocet na dorazenie do tejto pozicie je {minimumMovements}"

def passed_through_start(movements): #kontrola ci prejde cez start
    listOfMovements = []
    stepByStep = []
    currentPosition = [0, 0]

    for i in range(len(movements)):
        listOfMovements.append(movements[i]) 
                                #^ tu bola chyba, bolo tam listOfMovements.append(i), co len pridavalo cislo indexu
                                #a tym bola tato funkcia nefunkcna-vzdy vratila True, pretoze neskorsie podmienky nic vlastne neskontrolovali, 
                                #takze nebola sanca vratit False

    for positionChange in listOfMovements: #tvori list pocas pohybu
        stepByStep.append(positionChange) #list sa meni po kazdom pohybu, skontroluje piziciu, ak je [0, 0], vrati True
        currentPosition[0] = axis_X(stepByStep)
        currentPosition[1] = axis_Y(stepByStep)
        if currentPosition == [0, 0]:
            return ("\nCestovateľ taktiež prešiel cez štart!", True)
    return ("\nCestovateľ neprešiel cez štart.", False) #ak predchadzajuci for loop zisti, ze sa cez start nepohne, vrati False - nepresiel cez start

def get_information(movements):
    if not is_valid(movements):
        raise ValueError("Nebol zadaný správny vstup. Beriem len vstupy ako napr SJVZ, bez medzier, len velke inicialy.")
        
    noOfMovements = movements_count(movements)
    newPosition = new_position(movements)
    minReqMovements = minimum_movements(movements)
    passedStart = passed_through_start(movements)
    
    return f"Cestovateľ skončil na súradniciach {newPosition}. \nCestovateľ sa spolu pohol {noOfMovements}-krát. \nNa to, aby sa cestovateľ dostal na koniec sa musí pohnúť minimálne {minReqMovements}. {passedStart[0]}"
    
try:
    results = get_information(vstup)
    print(results)
except ValueError as chyba:
    print(chyba)



        
    