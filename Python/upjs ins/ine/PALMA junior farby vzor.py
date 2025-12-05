def zisti_farbu(r, g, b):
    farby = [
        [0, 0, 0, 'black'],
        [0, 0, 127, 'navy blue'],
        [0, 0, 255, 'blue'],
        [0, 127, 0, 'hulk'],
        [0, 127, 127, 'teal'],
        [0, 127, 255, 'azure'],
        [0, 255, 0, 'green'],
        [0, 255, 127, 'guppie green'],
        [0, 255, 255, 'aqua'],
        [127, 0, 0, 'maroon'],
        [127, 0, 127, 'purple'],
        [127, 0, 255, 'violent violet'],
        [127, 127, 0, 'drably olive'],
        [127, 127, 127, 'platinum granite'],
        [127, 127, 255, 'blue party parrot'],
        [127, 255, 0, 'radium'],
        [127, 255, 127, 'light green'],
        [127, 255, 255, 'electric blue'],
        [255, 0, 0, 'red'],
        [255, 0, 127, 'rose'],
        [255, 0, 255, 'magenta'],
        [255, 127, 0, 'orange juice'],
        [255, 127, 127, 'light red'],
        [255, 127, 255, 'hottest of pinks'],
        [255, 255, 0, 'yellow'],
        [255, 255, 127, 'ecuadorian banana'],
        [255, 255, 255, 'white'],
    ]

    najblizsiNazov = None
    najmensiaVzdialenost = float('inf')

    for R, G, B, nazov in farby:
        dr = R - r
        dg = G - g
        db = B - b
        vzdialenost = dr * dr + dg * dg + db * db

        if vzdialenost < najmensiaVzdialenost:
            najmensiaVzdialenost = vzdialenost
            najblizsiNazov = nazov

    return najblizsiNazov
