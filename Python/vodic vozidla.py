cesta = ["zo", 20, 30, 50, "zd", 80, 90, "ko", 100, 120, 130, "kd", 100, 90]
#   trochu modifikovane pre testovanie
#   funguje len za predpokladu, ze len raz vojde a vyjde z obce a ze len raz prejde a vyjde z dialnice
#   

obecLimit = 50
noBothLimit = 90
highwayLimit = 130

def is_in_range(start, end, index):
    if start < index < end:
        return True
    else:
        return False


def is_speeding(roadLog):
    obecStart = 0
    obecEnd = roadLog.index(roadLog[-1])
    obecOnly = []

    highwayStart = 0
    highwayEnd = roadLog.index(roadLog[-1])
    highwayOnly = []
    
    noBothOnly = []

    for position in range(len(roadLog)):
        if type(roadLog[position]) == str:
            if roadLog[position] == "zo":
                obecStart = position
            elif roadLog[position] == "ko":
                obecEnd = position
            elif roadLog[position] == "zd":
                highwayStart = position
            elif roadLog[position] == "kd":
                highwayEnd = position

    for position in range(len(roadLog)):
        if type(roadLog[position]) == int:
            if is_in_range(obecStart, obecEnd, position):
                if is_in_range(highwayStart, highwayEnd, position):
                    noBothOnly.append(roadLog[position])
                else:
                    obecOnly.append(roadLog[position])

            elif is_in_range(highwayStart, highwayEnd, position):
                highwayOnly.append(roadLog[position])

            elif not is_in_range(highwayStart, highwayEnd, position) and not is_in_range(obecStart, obecEnd, position):
                noBothOnly.append(roadLog[position])
    
    for obec in obecOnly:
        if obec > obecLimit:
            return True, "Prekročil limit v obci!", obec
    
    for highway in highwayOnly:
        if highway > highwayLimit:
            return True, "Prekročil limit na diaľnici!", highway
        
    for noBoth in noBothOnly:
        if noBoth > noBothLimit:
            return True, "Prekrocil limit na diaľnici v obci alebo mimo obce a dialnice!", noBoth
    
    return False, "Rýchlostný limit neprekročil ani raz! Vodič nemá rád pokuty."

print(is_speeding(cesta))