ceny = [34, 32, 30, 35, 33, 32, 38, 40, 37]

class ObchodSoZlatom():
    def __init__(self, zlato, peniaze):
        self.__zlato = zlato
        self.__peniaze = peniaze
    
    def getPeniaze(self):
        return self.__peniaze
    
    def getZlato(self):
        return self.__zlato
    
    def predajZlato(self, cenaZlata):
        self.__peniaze = self.__zlato * cenaZlata
        self.__zlato = 0

    def kupZlato(self, cenaZlata):
        self.__zlato = self.__peniaze / cenaZlata
        self.__peniaze = 0
    
    def vypis(self):
        print(f"Peniaze: {self.getPeniaze()}€\nZlato: {self.getZlato()}g")

def simulujPriebehObchodu(ceny:list, penazenka:ObchodSoZlatom):
    for i in range(len(ceny) - 1):
        if ceny[i] > ceny[i + 1]: # ak dnes je drahsie ako zajtra, chcem predat
            if penazenka.getZlato() != 0:
                penazenka.predajZlato(ceny[i])
        elif ceny[i] < ceny[i + 1]: # ak dnes je lacnejsie ako zajtra, chcem kupit
            if penazenka.getPeniaze() != 0:
                penazenka.kupZlato(ceny[i])

mojaPenazenka = ObchodSoZlatom(0, 300)

simulujPriebehObchodu(ceny, mojaPenazenka)
mojaPenazenka.vypis()