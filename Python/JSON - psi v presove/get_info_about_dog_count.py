import os
import json


def create_file_paths():
    global DIR_folderPath 
    global ABSPATH_dataFilePath 
    global ABSPATH_dogsPerStreet
    global ABSPATH_organizedFIle 
    global data
    DIR_folderPath = os.path.dirname(__file__)
    ABSPATH_dataFilePath = os.path.join(DIR_folderPath, "Zoznam_Počet_prihlásených_psov_podľa_adresy_chovu_psa.json")
    ABSPATH_dogsPerStreet = os.path.join(DIR_folderPath, "Dogs per street.txt")
    ABSPATH_organizedFIle = os.path.join(DIR_folderPath, "Data organized.txt")
    with open(ABSPATH_dataFilePath, "r", encoding="utf-8") as file:
        data = json.load(file)
create_file_paths()

def get_dog_count_per_street(myData: dict): #len ulice bez organizovania do casti mesta
    streetDogDict = {}
    streetName = ""
    for section in myData:
        streetName = section["Ulica_(chovu_psa)"]
        if section["Ulica_(chovu_psa)"] not in streetDogDict: #ak neni kluc, vytvori ho
            streetDogDict[streetName] = 0
        streetDogDict[streetName] += int(section["Počet_psov"]) #prida pocet psov na ulici
    
    return streetDogDict    

def get_total_dog_count(myData: dict): 
    dogCount = sum([int(section["Počet_psov"]) for section in myData])
    return dogCount

def get_dog_count_data(myData: dict): #analyza a organizovanie dat
    '''
    Štruktúra: {key:(dict}, key:{dict}, ...}
    '''
    streetName = ""
    catStreets = {} #categorizedStreets
    regionName = ""
    for section in myData:
        streetName = section["Ulica_(chovu_psa)"]
        regionName = section["Časť_mesta"]
        if section["Časť_mesta"] not in catStreets.keys():
            catStreets[regionName] = {}
        if section["Ulica_(chovu_psa)"] not in catStreets[regionName].keys():
            catStreets[regionName][streetName] = 0
        catStreets[regionName][streetName] += int(section["Počet_psov"])

    return catStreets

def finalize_data(myData: dict): #prepisanie dat pre zapisanie do suboru
    myTrans = str.maketrans("()',[]", "   :  ")
    finalData = ""
    for item in myData.keys():
        newData = str(list(myData[item].items()))
        Data1 = newData.replace("),", "\n    ").replace(" :", ":")
        Data2 = item + ":\n    " + Data1.translate(myTrans) + "\n\n"
        finalData += Data2
    return finalData
    
def get_amount_of_dogs_on_strt(myData: dict, street: str):
    specialResponses = ["n", "z"]

    while street in specialResponses:
        if street == "n":
            return "Ulicu ste zvolili nezadať.\n"
        elif street == "z":
            avlblStreets = f"Zoznam ulíc: {get_dog_count_per_street(myData).keys()}]"
            print(avlblStreets)
            street = input("Zadajte celý názov ulice na ktorej chcete nájsť počet psov (ak nechcete túto informáciu, zadajte písmeno n): ")
    
    if street not in get_dog_count_per_street(myData).keys():
        return "Nebol zadaný správny vstup!\n"

    return f"Na tejto ulici ({street}) je {get_dog_count_per_street(myData)[street]} psov.\n"

def write_partial_data(myData: dict):
    myTrans = str.maketrans(r"()',{}", r"   :  ")
    streetDogList1 = get_dog_count_per_street(myData).items() 
    streetDogList2 = list(map(str, streetDogList1))
    streetDogList3 = ["Ulica: " + item + "\n" for item in streetDogList2]
    streetDogList4 = "".join(streetDogList3)
    streetDogListFinal = streetDogList4.translate(myTrans)
    return streetDogListFinal
    
def find_most_dogs(myData: dict):
    newData = write_partial_data(myData)
    dogsPerStreet = newData.split("\n")[:-1]
    listOfDogs = [item.split(":") for item in dogsPerStreet]
    listOfDogs2 = [item[-1] for item in listOfDogs]
    listOfDogsFinal = [int(item) for item in listOfDogs2] #dalo by sa do 1 riadku, nechce sa mi, toto sa lahsie prepisuje
        
    return(dogsPerStreet[listOfDogsFinal.index(max(listOfDogsFinal))])