import tkinter as tk

MAX_WIDTH = 900
MAX_HEIGHT = 600

HRUBKA_STENY = 100
ZACIATOK_MURU_X = MAX_WIDTH - HRUBKA_STENY
ZACIATOK_MURU_Y = 0
KONIEC_MURU_X = 0 + MAX_WIDTH
KONIEC_MURU_Y = 0 + MAX_HEIGHT

HRUBKA_CESTY = 100
ZACIATOK_CESTY_X = 0 + HRUBKA_CESTY
ZACIATOK_CESTY_Y = MAX_HEIGHT - HRUBKA_CESTY
KONIEC_CESTY_X = MAX_WIDTH - HRUBKA_STENY
KONIEC_CESTY_Y = MAX_HEIGHT

root = tk.Tk()
root.title("Cuvanie")

canvas = tk.Canvas(root, bg="white", width=MAX_WIDTH, height=MAX_HEIGHT)
canvas.pack()

class Auto():
    def __init__(self) -> None:
        # nastav rozmery auta
        self.autoSirka = 100
        self.autoVyska = 60
        self.autoX1 = ZACIATOK_CESTY_X # predok
        self.autoY1 = ZACIATOK_CESTY_Y - 10 - self.autoVyska # vrch
        self.autoX2 = self.autoX1 + self.autoSirka # zadok
        self.autoY2 = ZACIATOK_CESTY_Y - 10 - self.autoVyska + self.autoVyska # spodok
        #

        # poloz auto
        self.auto = canvas.create_rectangle(self.autoX1, self.autoY1, self.autoX2, self.autoY2, fill="violet")

        # chceme aj indikator
        self.polozIndikator()
    
    def polozIndikator(self):
        # nastav rozmery indikatora
        self.indikatorPolomer = 15
        self.indikatorX1 = self.autoX2 - self.indikatorPolomer*2 - 3
        self.indikatorY1 = self.autoY1 + (self.autoVyska / 4) 
        self.indikatorX2 = self.indikatorX1 + (2 * self.indikatorPolomer)
        self.indikatorY2 = self.indikatorY1 + (2 * self.indikatorPolomer)
        # vypocitaj aj vzdialenost od steny
        self.vzdialenost = self.vypocitajVzdialenostOdSteny()
        # zapis aj info o vzdialenosti
        self.vypis = canvas.create_text(100, 100, fill="red", text=f"{self.vzdialenost}", font=("Calibri", 12))
        # rozhodni sa o farbe
        self.indikatorFarba = self.rozhodniOFarbe()
        
        self.indikator = canvas.create_oval(self.indikatorX1, self.indikatorY1, self.indikatorX2, self.indikatorY2, fill=self.indikatorFarba)

    def vypocitajVzdialenostOdSteny(self):
        return ZACIATOK_MURU_X - self.autoX2
    
    def rozhodniOFarbe(self):
        if self.vzdialenost < 60:
            farba = "red"
        elif 300 >= self.vzdialenost and self.vzdialenost >= 60:
            farba = "orange"
        else:
            farba = "green"
        return farba
    
    def pohniAuto(self, udalost):
        # poloz auto
        self.autoX2 = udalost.x
        self.autoX1 = self.autoX2 - self.autoSirka
        canvas.moveto(self.auto, self.autoX2 - self.autoSirka, self.autoY1)

        # poloz indikator
        canvas.delete(self.indikator)
        canvas.delete(self.vypis)
        self.polozIndikator()

def cestaSMurom() -> None:
    # cesta
    canvas.create_rectangle(ZACIATOK_CESTY_X, ZACIATOK_CESTY_Y, KONIEC_CESTY_X, KONIEC_CESTY_Y, fill="black")
    # mur
    canvas.create_rectangle(ZACIATOK_MURU_X, ZACIATOK_MURU_Y, KONIEC_MURU_X, KONIEC_MURU_Y, fill="black")

naseAuto = Auto()

def pohniAuto2(udalost):
    naseAuto.pohniAuto(udalost)

canvas.bind("<Button-1>", pohniAuto2)

# TODO dorobit pravitko

def nakresliPravitko():
    # najprv ciara
    canvas.create_rectangle(ZACIATOK_CESTY_X, ZACIATOK_CESTY_Y + (HRUBKA_CESTY/2) + 2, KONIEC_CESTY_X, ZACIATOK_CESTY_Y + (HRUBKA_CESTY/2) - 2, fill="red")
    stredPravitka = ZACIATOK_CESTY_Y + (HRUBKA_CESTY/2)
    for i in range(0, KONIEC_CESTY_X - HRUBKA_CESTY, 30):
        canvas.create_text(ZACIATOK_CESTY_X + i, stredPravitka + 10, fill="red", text=f"{700 - i}", font=("Calibri", 12))

cestaSMurom()
nakresliPravitko()
root.mainloop()