def get_input_info():
    dom_rozmery = input()
    dom_mapa = ""
    for _ in range(int(dom_rozmery[0])):
        dom_mapa += input()
        dom_mapa += "\n"
    dom_mapa = dom_mapa[:-1].split("\n")
    house_height = int(dom_rozmery[0]) - 1
    house_width = int(dom_rozmery[2]) - 1
    if not 1 <= house_height <= 10: return
    if not 1 <= house_width <= 10: return

    #print(dom_mapa)

    pozemok_rozmery = input()
    pozemok_mapa = ""

    for _ in range(int(pozemok_rozmery[0])):
        pozemok_mapa += input()
        pozemok_mapa += "\n"
    pozemok_mapa = pozemok_mapa[:-1].split("\n")
    land_height = int(pozemok_rozmery[0]) - 1
    land_width = int(pozemok_rozmery[2]) - 1
    if not house_height <= land_height <= 50: return
    if not house_width <= land_width <= 50: return
    #print(pozemok_mapa)
    return dom_mapa, house_height, house_width, pozemok_mapa, land_height, land_width

user_input = get_input_info()

dom_mapa, house_height, house_width, pozemok_mapa, land_height, land_width = user_input[0], user_input[1], user_input[2], user_input[3], user_input[4], user_input[5]

def place_houses(house, land):
    success_count = 0
    houses_built = []

    for land_layer, land_row in enumerate(land[:]):
        if land_layer > land_height - house_height: # ak sme medzi vrchom a najspodnejsou moznou castou pozenmku, staviame dom
            break
        
        if house[0] in land_row: # 1. cast domu
            parts_built = 0
            start_position = land_row.index(house[0])
            for house_layer, house_row in enumerate(house): # casti domu od 2. po koniec
                if (house_row in (first:=(land[land_layer+house_layer])[start_position : start_position + house_width + 1])) or (house_row in (second:=(land[land_layer+house_layer])[start_position : start_position + house_width + 1].replace(".", "x"))):
                    houses_built.append(first.count(house_row) or second.count(house_row))
                    parts_built += 1 # pocita iteracie vnutorneho for loopu
                    if parts_built == house_height: # ked sa rovnaju, postavil sa cely dom, koniec iteracie vonkajsieho for loopu
                        success_count += 1
                        print(success_count, "check")
                        parts_built = 0
                else:
                    parts_built = 0

    print(success_count, "program end")
    print(houses_built)


place_houses(dom_mapa, pozemok_mapa)