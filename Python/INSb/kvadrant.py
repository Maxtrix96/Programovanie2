citatele = [0] * (10_240 / 2)

vstup = "((VVVF)VVV)"

def vyplnTabulku():
    mocnina = 0
    for i in range(len(vstup)):
        znak = vstup[i]
        if znak == '(':
            mocnina += 1
        elif znak == ')':
            mocnina -= 1
        elif znak == 'F':
            citatele[i] += 1

def najdiNajvacsiMenovatel():
    for i in range(len(citatele), 0, - 1):
        pass

# DU