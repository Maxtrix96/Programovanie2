pole = [1, 2, 3, 4]
n = len(pole)

DP = [[None for i in range(n)] for i in range(n)]
for i in range(n):
    DP[i][i] = pole[i]*n

def sucet(od, do):
    if DP[od][do] is None:
        poradie = od + n - do
        DP[od][do] = max(sucet(od + 1, do) + pole[od] * poradie, sucet(od, do - 1) + pole[do] * poradie)
    return DP[od][do]

print(sucet(0, n-1))