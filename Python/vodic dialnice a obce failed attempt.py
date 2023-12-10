cesta = [60, "zo", 20, 30, 50, "zd", 80, 90, "ko", 100, 120, 130, "kd", 100, 90]

#   zo = zaciatok obce
#   ko = koniec obce
#   zd = zaciatok dialnice
#   kd = koniec dialnice

commLimit = 50
highwayLimit = 130
neitherBothLimit = 90

def get_com(roadLog):
    commStart = 0
    commEnd = 0
    comm = []
    
    for item in roadLog:
        if item == "zo":
            commStart = roadLog.index(item)
        if item == "ko":
            commEnd = roadLog.index(item)
    
    comm = roadLog[commStart+1:commEnd]

    for item in comm:
        if type(item) != int:
            comm[comm.index(item)] = 0
    
    return comm
        
def get_highway(roadLog):
    highwayStart = 0
    highwayEnd = 0
    highway = []
    
    for item in roadLog:
        if item == "zo":
            highwayStart = roadLog.index(item)
        if item == "ko":
            highwayEnd = roadLog.index(item)
    
    highway = roadLog[highwayStart+1:highwayEnd]

    for item in highway:
        if type(item) != int:
            highway[highway.index(item)] = 0
    
    return highway

def get_sections(roadLog):
    '''
    :return: tuple[0] - commLog, tuple[1] - highwayLog, tuple[2] - neitherBothLog
    '''
    highwayStart = 0
    highwayEnd = 0
    highwayLog = []
    
    for item in roadLog:
        if item == "zo":
            highwayStart = roadLog.index(item)
        if item == "ko":
            highwayEnd = roadLog.index(item)
    
    highwayLog = roadLog[highwayStart+1:highwayEnd]

    for item in highwayLog:
        if type(item) != int:
            highwayLog[highwayLog.index(item)] = 0

    commStart = 0
    commEnd = 0
    commLog = []
    
    for item in roadLog:
        if item == "zo":
            commStart = roadLog.index(item)
        if item == "ko":
            commEnd = roadLog.index(item)
    
    commLog = roadLog[commStart+1:commEnd]

    for item in commLog:
        if type(item) != int:
            commLog[commLog.index(item)] = 0

    neitherBothLog = []

    for item in roadLog:
        itemIndex = roadLog.index(item)
        if itemIndex < commStart and itemIndex < highwayStart:
            neitherBothLog.append(item)
        if itemIndex > commEnd and itemIndex > highwayEnd:
            neitherBothLog.append(item)
        if itemIndex > commStart and itemIndex > highwayStart:
            if itemIndex < commEnd and itemIndex < highwayEnd:
                neitherBothLog.append(item)
    
    return(commLog, highwayLimit, neitherBothLog)



def find_speeding(roadLog):
    commLog = get_sections(roadLog)[0]
    highwayLog = get_sections(roadLog)[1]
    combinedLog = get_sections(roadLog)[2]

    for speed in commLog:
        if speed > commLimit:
            return (True, 0)
    for speed in highwayLog:
        if speed > highwayLimit:
            return (True, 1)
    for speed in combinedLog:
        if speed > combinedLog:
            return (True, 2)
    
    return (False, 3)
        
print (find_speeding(cesta))


