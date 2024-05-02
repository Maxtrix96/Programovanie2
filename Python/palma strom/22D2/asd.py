input_number = 0
vstup = ""
dom_rozmery = input()
dom_mapa = ""
for i in range(int(dom_rozmery[0])):
    dom_mapa += input()
    dom_mapa += "\n"
dom_mapa = dom_mapa[:-1].split("\n")
house_width = int(dom_rozmery[2])

#print(dom_mapa)

pozemok_rozmery = input()
pozemok_mapa = ""

for i in range(int(pozemok_rozmery[0])):
    pozemok_mapa += input()
    pozemok_mapa += "\n"
pozemok_mapa = pozemok_mapa[:-1].split("\n")
land_width = int(pozemok_rozmery[2])
#print(pozemok_mapa)

def place_house(house, land):
    for row in land:
        if house[0] in row:
            pass

