mapa = [[znak for znak in riadok] for riadok in '''
...........
...........
....#......
....#......
....#.#....
....#.#....
..S...#.C..
......#....
'''.split()]
n, m = len(mapa), len(mapa[0])
rS, sS = 6,2
rC, sC = 6,8

def zobraz_bludisko(mapa):
    for riadok in mapa:
        print(*riadok)

def da_sa(riadok, stlpec):
    if 0 <= riadok < n and 0 <= stlpec < m:
        return mapa[riadok][stlpec] == '.'
    
    return False

pohyby = [(0, 1), (0, -1), (1, 0), (-1, 0)]

r, s = 6, 2
def zrob_pohyb():
    for pos_r, pos_s in pohyby:
        novy_r, novy_s = r+pos_r, s+pos_s
        if (da_sa(novy_r, novy_s)):
            mapa[novy_r, novy_s] = mapa[r][s] + 1

# na INSb stranke


from queue import Queue

pohyby = [(0,1), (0, -1), (1, 0), (-1, 0)]
mapa = [[znak for znak in riadok] for riadok in '''
...........
...........
....#......
....#......
....#.#....
....#.#....
......#....
......#....
'''.split()]
n, m = len(mapa), len(mapa[0])
rS, sS = 6,2
rC, sC = 6,8
mapa[rS][sS] = 0
rad = Queue()
rad.put( (rS, sS) )
mapa[rS][sS] = 0
#mapa[rC][sC] = 
while not rad.empty():
    r, s = rad.get() #vyberie = odstrani
    if (r, s) == (rC, sC):
        break
    for pos_r, pos_s in pohyby:    
        novy_r, novy_s = r+pos_r, s+pos_s
        if da_sa(novy_r, novy_s):
            mapa[novy_r][novy_s] = mapa[r][s]+1
            
            rad.put( (novy_r, novy_s) )
print(mapa[rC][sC])            
zobraz_bludisko(mapa)