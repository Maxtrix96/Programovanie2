def zrotuj(znaky, kluc)
    if kluc>0:
      kluc = kluc % len(znaky)
    if kluc<0:
      -kluc = -kluc % len(znaky) 
    return s[k:] + s[:k]
    
def desifruj(odpoved, kluc):
    parne_znaky = odpoved[::2]  # Párne indexy (0, 2, 4,...)
    neparne_znaky = odpoved[1::2]  # Nepárne indexy (1, 3, 5,...)

    parne_zrotovane = zrotuj(parne, kluc)
    neparne_zrotovane = zrotuj(neparne, -kluc)

    desifrovane = ""
    index_parne, index_neparne = 0, 0
    for i in range(len(odpoved)):
        if i % 2 == 0:
            desifrovane += parne_zrotovane[index_parne]
            parne += 1
        else:
            desifrovane += neparne_zrotovane[index_neparne]
            neparne += 1

    return desifrovane

odpoved = RTAKINIOFM  
kluc = 3 
desifrovane = desifruj(odpoved, kluc)
print("Dešifrovaný text:", desifrovane)