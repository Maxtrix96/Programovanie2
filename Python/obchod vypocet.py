tovar = ["jablko cervene", "ovocny caj", "jablko cervene", "jastrab", "jastrab"]
cena = [0.98, 1.12, 0.98, 1.5, 1.5]
pocet = [1.13, 2, 2.12, 2, 2]



def get_shopping_info(tovar, cena, pocet):
    '''
    Vypocita info, vrati string 

    :param tovar: list s produktmi
    :param cena: list s cenami, float/int
    :param pocet: kolko produktu, float/int
    :return: string so stringmi vnutri, index 0 - produkt, index 1 - kolko, index 2 - kolko zaplatit za produkt 
    '''

    itemsBought = []
    tempCategory = [] 

    for i in range(len(tovar)):
        tempCategory = ["", 0.0, 0.0] #co, kolko, spolu cena
        tempCount = 0
        tempCategory[0] = tovar[i]
        tempCategory[1] = pocet[i]
        tempCategory[2] = cena[i] * pocet[i]
        itemsBought.append(tempCategory)

        for itemInfo in itemsBought: #pozrie kazdi substring s info
            if itemInfo[0] == tovar[i]: #hlada duplikat, ak najde, odstrani duplikat a ciselne hodnoty originalu aktualizuje
                tempCount += 1 
                if tempCount > 1:
                    itemCount = itemInfo[1]
                    itemTotal = itemInfo[2]
                    for original in itemsBought: #najde original a aktualizuje hodnoty v indexoch 1 a 2
                        if original[0] == itemInfo[0]:
                            original[1] += itemCount
                            original[2] += itemTotal
                    itemsBought.pop() #odstrani najnovsiu hodnotu - duplikat sa efektivne spoji s originalom

    return itemsBought

shopping = get_shopping_info(tovar, cena, pocet)
print(shopping)