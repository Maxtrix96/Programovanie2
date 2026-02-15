def desifruj(sifraString:str) -> str: 
    # najtazsia cast ulohy: vediet spoluhlasky
    spoluhlasky:str = "bcčdďfghjklľmnňprsštťvzžBCČDĎFGHJKLĽMNŇPRSŠTŤVZŽ"
    # lahsie pracovat so zoznamom
    sifra:list = [c for c in sifraString]
    # predpokladajme spoluhlasku na konci
    idxSpoluhlaskyVzadu:int = len(sifra) -1
    # ideme od zaciatku az po stred, resp. po idx tesne pred stredom, cize zahadzujeme desatine cislo ak ma neparny pocet znakov
    idxStredu:int = int(len(sifra) / 2) - 1 if len(sifra) % 2 == 0 else int(len(sifra) / 2)
    for i in range(idxStredu): # vratne toho indexu
        if sifra[i] in spoluhlasky:
            # hladaj sifru na druhej strane od poslednej najdenej spoluhlasky
            for j in range(idxStredu, idxSpoluhlaskyVzadu + 1)[::-1]:
                if sifra[j] in spoluhlasky:
                    sifra[i], sifra[j] = sifra[j], sifra[i]
                    idxSpoluhlaskyVzadu = j - 1
                    break

    return "".join(sifra)

print(desifruj("rAnjA MuLioP"))
print(desifruj("vek"))
print(desifruj("vekin"))
print(desifruj("daniel sabol"))
print(desifruj("labiel sanod"))
print(desifruj("kmn"))