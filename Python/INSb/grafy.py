#vrcholy si interne precislujeme od NULY
vstup = ['1 2',
'2 6',
'2 7',
'3 5',
'4 5',
'4 6',
'6 7',
'7 8',
'8 9',
'8 10',
'11 12',
'11 13',
'12 14',
'13 14']

n = 14
m = 14

susedia = [ [] for _ in range(n) ] #zoznam susedov pre kazdy vrchol
# for _ in range(m):
for i in range(len(vstup)):
    x, y = [int(_)-1 for _ in vstup[i].split() ] #ocislujeme od nuky
    susedia[x].append(y)
    susedia[y].append(x)
print(*susedia) #zoznam susedov


from queue import Queue

rad = Queue()

navstiveny = [False]*n
rad.put(3) # vlozit zaciatok

while not rad.empty():
    vrchol = rad.get() # vybrat
    # spracovat vs. susedov, kt. este neboli
    navstiveny[vrchol] = True
    # pridame vs. nenavstivenych susedov
    for sused in susedia[vrchol]:
        if navstiveny[sused] == False: # <=> if not navstiveny[sused]
            rad.put(sused)
    print(vrchol)