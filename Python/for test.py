program = int(input("Chcel/-a by si zistiť ako koľvek veľkú násobilku akú chceš? Zadaj 0 ak áno, hocičo iné ak nie"))
if program != 0:
    print("Tak prečo si tu? Nechaj ma napokoji!")

while True:
    while program == 0:
        x = int(input("Zadaj akú veľkú násobilku chceš (10, 20, 5...)"))
        y = int(input("Zadaj po ktoré číslo mám násobiť."))
        for i in range(x):
            print(i+1 , ": ", end=" ")
            for j in range(y):
                print((i+1)*(j+1), end=" ")
            print(" ")
        break
    program = int(input("Chcel/-a by si zistiť ako koľvek veľkú násobilku akú chceš? Zadaj 0 ak áno, hocičo iné ak nie"))
    if program != 0:
        break
