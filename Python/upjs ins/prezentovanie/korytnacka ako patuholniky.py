import turtle as t

# skolske kolo 10. rocnika, 1. uloha

obrazovka = t.Screen()
f = t.Turtle()

def patUholnik(dlzka): 
    # pomocna funkcia pre kreslenie koncatin, pre cistotu, citatelnost a udrzatelnost kodu
    for _ in range(5):
        f.forward(dlzka)
        f.left(360 / 5) # o kolko sa ma otocit? vnutorny uhol pri 1 vrchole je vzdy 360 / pocet stran (vrcholov)

def poly5(dlzka): 
    for _ in range(5):
        f.forward(dlzka / 3)
        patUholnik(dlzka / 3)
        # po nakresleni hlavy/nohy si treba uvedomit, ze sme tam, kde sme zacali
        f.forward(dlzka * 2 / 3)
        f.right(360 / 5) # nezabudni sa otocit

def start():
    poly5(90)

start()
poly5(200)

obrazovka.mainloop()