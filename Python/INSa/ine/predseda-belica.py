import random
import tkinter as tk

# kalendar zo šk. r. 25/26

pocetZiakov:int = int(input("Zadaj pocet ziakov: "))
ziaci:list[int] = [0] * pocetZiakov
pocetTyzdnov:int = 21
dni:list[int] = [0] * (pocetTyzdnov * 7)


def simulaciaSkolskehoRoka() -> None:
    # prechadzame kazdym tyzdnom
    for tyzden in range(pocetTyzdnov):
        pocetPracovnychDni:int = 7
        # rozhodni, kolko pracovnych dni je v danom tyzdni
        if tyzden == 1: # 1
            pocetPracovnychDni = 4
        elif tyzden == 5: # 4
            pocetPracovnychDni = 1
        elif tyzden == 9: # 2
            pocetPracovnychDni = 3
        elif tyzden == 10: # 2
            pocetPracovnychDni = 3
        elif tyzden == 13: # 1
            pocetPracovnychDni = 4
        elif tyzden == 14: # 1
            pocetPracovnychDni = 4

        # vypis tyzden
        print(f"{tyzden + 1}. tyzden: ")

        for den in range(pocetPracovnychDni):
            # vyber predsedu triedy a pripocitaj jeho pocet
            predsedaTriedy:int = random.randrange(0, pocetZiakov)
            ziaci[predsedaTriedy] += 1
            # vypis do konzole udaje o danom dni
            print(f"{den + 1}. den: {predsedaTriedy + 1}", end=" | ")
        # pridaj este 2 nove riadky pre dalsi cyklus a pre krasotu
        print("\n")
    
    # este ze ktory ziak kolko krat
    for i in range(len(ziaci)):
        print(f"{i + 1}. ziak: {ziaci[i]}", end=" | ")

simulaciaSkolskehoRoka()