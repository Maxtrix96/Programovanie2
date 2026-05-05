from queue import PriorityQueue

def najlacnejsia_kostra(susedia:dict, start:str):
    pr = PriorityQueue() #prioritny rad

    zoznam_navstivenych = []
    navstiveny = {key:False for key in susedia.keys()}

    pr.put( (0, None, start) ) #vlozime kde chceme zacat

    cena = 0
    kostra = []
    while not pr.empty():
        vzdialenost, skade, kam = pr.get() #vyberie najmensiu hranu z daneho radu
        if not navstiveny[kam]: #ak sme tento vrchol este nespracovali
            if not skade is None:
                print(f'{skade} - {kam}: {vzdialenost}')
                cena += vzdialenost
                #kostra.append(f'{skade}{kam}')
                kostra.append(skade+kam)
            navstiveny[kam] = True
            #pridame hrany z vrchola kam
            for sused in susedia[kam]:
                if not navstiveny[sused]:
    #                print(f'... {kam} {sused} {susedia[kam][sused]}')
                    pr.put( (susedia[kam][sused], kam, sused) )             
    return (cena, kostra) 

susedia = {'A': {'B': 4, 'H': 6},
 'B': {'A': 4, 'C': 9, 'E': 2, 'H': 5},
 'C': {'B': 9},
 'D': {'E': 15},
 'E': {'B': 2, 'D': 15, 'F': 8},
 'F': {'E': 8, 'G': 3, 'H': 10},
 'G': {'F': 3, 'H': 14},
 'H': {'A': 6, 'B': 5, 'F': 10, 'G': 14}}

print(najlacnejsia_kostra(susedia, 'E'))

