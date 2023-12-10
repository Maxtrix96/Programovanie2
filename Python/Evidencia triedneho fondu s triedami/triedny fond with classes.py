import os


def main():
    fileDirectory = os.path.dirname(__file__)

    class Triedny_Fond:
        def __init__(self, fileName: str) -> None:
            '''
            fileName bez.txt
            ''' 
            self.__originalDataPath = os.path.join(fileDirectory, f"{fileName} original.txt")
            self.__dataPath = os.path.join(fileDirectory, f"{fileName}.txt")
            self.__finalizedPath = os.path.join(fileDirectory, f"{fileName} finalized.txt")
            try:
                with open(self.__originalDataPath, "r", encoding="utf-8") as file:
                    self.__data = file.read()
            except FileNotFoundError:
                raise FileNotFoundError(f"Nebol zadaný správny názor súboru! [class.__init__()]\nZadali ste: {fileName}")
            self.__organize(self.__data)
            
        def __organize(self, data) -> None:
            '''
            spracuje dáta, len pre vnútorné pouzitie
            '''
            try:
                self.__transactionLog = [item.split(",") for item in data.split("\n")]
                self.__transDict = {}
                for item in self.__transactionLog:
                    if item[0] not in self.__transDict:
                        self.__transDict[item[0]] = 0
                    self.__transDict[item[0]] += float(item[1])
            except ValueError:
                raise ValueError("Nebol zadaný správny vpis! [class.__organize()]\nSprávny vpis: Meno, suma\nnapr. Jano, 8")
            
            #if "Zostatok" in self.__transDict:
            #    del self.__transDict["Zostatok"]
            #self.__transDict["Zostatok"] = sum(self.__transDict.values())
            #self.__total = self.self.__transDict["Zostatok"]
            self.__total = sum(self.__transDict.values())

        def append_transaction(self, inputData: str) -> None: 
            '''
            pripíse transakciu na koniec suboru (napr. pre fond1 to je triedny fond 1.txt) a do slovnika s datami o transakciach
            forma: "Meno, suma"
            '''
            with open(self.__dataPath, "w", encoding="utf-8") as file:
                self.__data += f"\n{inputData}"
                file.write(self.__data)

            self.__organize(self.__data)
        
        def get_person_data(self, person: str) -> float: 
            '''
            len meno cloveka
            '''
            return self.__transDict[person]
        
        def get_list_of_members(self) -> list: 
            '''
            vrati zoznam ludi, ktory sa podielaju na triendom fonde
            '''
            return list(self.__transDict.keys())
        
        def write_final_log(self) -> None: 
            '''
            zapise do suboru finalized.txt vysledok prevodov penazi
            '''
            with open(self.__finalizedPath, "w", encoding="utf-8") as file:
                self.__transFinal = "\n".join([item.replace("[", "").replace("]", "").replace("'", "") for item in list(map(str, [list(item) for item in list(self.__transDict.items())]))]).replace(", ", ", +").replace(", +-", ", -")
                file.write(self.__transFinal)

        def __str__(self) -> str:
            return f"{self.__total}"
            
        def __eq__(self, other) -> bool:
            return self.__total == other.__total
        

    def urob_zmeny():
        '''
        definujte si sami, co sa ma zo subormi stat
        '''
        fond1 = Triedny_Fond("triedny fond 1") # zadat nazov suboru, viac v README
        fond2 = Triedny_Fond("triedny fond 2")

        print("Karol: ", fond1.get_person_data("Karol"))
        fond1.append_transaction("Karol, 100")
        print("Karol: ", fond1.get_person_data("Karol"))
        fond1.append_transaction("Anton, +69")
        fond1.append_transaction("Mikulas, -350")
        print(fond1.get_list_of_members())

        print("Eve: ", fond2.get_person_data("Eve"))
        fond2.append_transaction("Eve, +100")
        print("Eve: ", fond2.get_person_data("Eve"))
        fond2.append_transaction("David, 69")
        print(fond2.get_list_of_members())

        fond1.write_final_log()
        fond2.write_final_log()

        print(f"fond1: {fond1}")
        print(f"fond2: {fond2}")
        print(fond1 == fond2)


    try:
        urob_zmeny()
    except FileNotFoundError as error:
        print(error)
    except ValueError as error2:
        print(error2)

main()