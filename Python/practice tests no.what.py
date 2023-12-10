#vyvtovirt program, ktory berie ako vstup 2 rovnako dlhe retazce
#z oboch vytvori jeden cely
#hodnoty v novom retazci sa budu strediat

string1 = "Andrea"
string2 = "Michal"

def mix_strings(string1, string2):
    listOfStr1 = []
    listOfStr2 = []
    combinedList = ""

    for i in range(len(string1)):
        listOfStr1.append(string1[i])
    for i in range(len(string2)):
        listOfStr2.append(string2[i])
    
    for i in range(len(string1)):
        combinedList += listOfStr1[i]
        combinedList += listOfStr2[i]
    
    return combinedList



#z kombinovaneho listu vytvor 2 povodne

def unmix_strings(mixedString): #"AMnidcrheaal"
    fixedString1 = ""
    fixedList1 = []
    fixedString2 = ""
    fixedList2 = []
    counter = 0
    mixedList = []

    for i in range(len(mixedString)):
        mixedList.append(mixedString[i])

    for letter in mixedList:
        fixedList1.append(letter)
        counter += 1
        if counter == 2:
            counter = 0
            fixedList1.pop()

    counter = 1

    for letter in mixedList:
        fixedList2.append(letter)
        counter += 1
        if counter == 2:
            counter = 0
            fixedList2.pop()

    for letter in fixedList1:
        fixedString1 += letter
    
    for letter in fixedList2:
        fixedString2 += letter
    
    return (fixedString1, fixedString2)



#definuj funkciu, ktoru zavolame s dvomi rozdelne dlhimi retazcami, ktora ich skonbinuje tak,
#ze sa v nej budu striedat hodnoty obidvoch retazcov, zvysne hodnoty z dlhsieho retazca zostanu na knoci 

def mix_different_strings(string1, string2):
    listOfStr1 = []
    listOfStr2 = []
    combinedString = string1 + string2
    longerList = []
    shorterList = []
    combinedList = []
    mixedList = []
    mixedString = ""

    for i in range(len(combinedString)):
        combinedList.append(combinedString[i])
    for i in range(len(string1)):
        listOfStr1.append(string1[i])
    for i in range(len(string2)):
        listOfStr2.append(string2[i])
    
    if len(listOfStr1) > len(listOfStr2):
        longerList = listOfStr1
        shorterList = listOfStr2
    elif len(listOfStr1) < len(listOfStr2):
        longerList = listOfStr2
        shorterList = listOfStr1
    elif len(listOfStr1) == listOfStr2:
        combinedList = mix_strings(string1, string2)
    
    for i in range(len(shorterList)):
        mixedList.append(shorterList[i])
        mixedList.append(longerList[i])
    for i in range(len(shorterList), len(longerList)):
        mixedList.append(longerList[i])
    print(mixedList)
    
    for letter in mixedList:
        mixedString += letter
    
    return mixedString

shorterString = "Diana"
longerString = "Ferdinand"

print(mix_different_strings(shorterString, longerString))