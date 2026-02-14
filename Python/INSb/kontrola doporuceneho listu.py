def kontrola_doporuceneho_listu(zadany_kod:str) -> bool:
    # retazec max. 30 znakov - zo zadania

    kod:str = "".join([(lambda l: l if l.isalnum() else "")(l) for l in zadany_kod]) # najprv sa zbavit medzier z kodu

    if len(kod) != 13: # spravny kod ma byt dlzky 2 + 8 + 1 + 2 = 13, ak nie, nie je to spravny kod
        return False

    if kod[0] == "R": # prvy znak ma byt R, alebo W 
        povolene_znaky:str = "QWERTYUIOPASDFGHJKLZXCVBNM"
        if not kod[1] in povolene_znaky: return False # ak je to R, druhy ma byt nejake pismeno z angl. abecedy, inak zly kod
    elif kod[0] == "W":
        if kod[1] != "E": return False # ak je to W ale nie E, zly kod
    
    if not (kod[-2] == "S" and kod[-1] == "K"): return False # posledne dve maju byt SK, inak zly kod

    # kontrola kontrolnej cislice: 
    #   n ak 1 <= n <= 9,
    #   0 ak n == 10,
    #   5 ak n == 11,
    #   kde n je zvysok vynasobenych cislic kodu po deleni 11
    ciselka:list[int] = [int(i) for i in kod[2:9+1]]
    vahy:list[int] = [8, 6, 4, 2, 3, 5, 9, 7]
    vynasobene_ciselka:list[int] = [i * j for i, j in zip(ciselka, vahy)]
    kontrolna_cislica_podla_vypoctu:int = 11 - (sum(vynasobene_ciselka) % 11)

    if int(kod[-3]) == kontrolna_cislica_podla_vypoctu: return True # ak sa cislica v kode rovna vypocitanemu, kod je OK

    return False # ak nie, zly kod

print(kontrola_doporuceneho_listu("RN343216886SK"))
print(kontrola_doporuceneho_listu("RN343216882SK"))
print(kontrola_doporuceneho_listu("AB343216886CZ"))
print(kontrola_doporuceneho_listu("RN 34 321 688 6 SK"))

def palma_evaluovaci_algoritmus() -> None:
    pocet_riadkov:int = int(input())
    if not 1 <= pocet_riadkov <= 1000: raise ValueError("Zadany zly pocet nasledujucich riadkov")

    zadane_kody:list[str] = []
    for _ in range(pocet_riadkov):
        vstup:str = input()
        zadane_kody.append(vstup)
    
    for s in zadane_kody:
        print(kontrola_doporuceneho_listu(s))
    
palma_evaluovaci_algoritmus()