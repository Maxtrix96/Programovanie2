citatele = [0] * 10

vstup = "((VVVF)VVV)" # -> 1/16

def vyplnTabulku():
    mocnina = 0
    for i in range(len(vstup)):
        znak = vstup[i]
        if znak == '(':
            mocnina += 1
        elif znak == ')':
            mocnina -= 1
        elif znak == 'F':
            citatele[mocnina] += 1

def najdiNajvacsiMenovatel():
    vyplnTabulku()
    idxNajvacsej = -1
    for i in range(len(citatele)): # najdi najvacsiu mocninu, kt. sa tam nachadza
        if idxNajvacsej < 0:
            if citatele[len(citatele) - 1 - i] > 0:
                idxNajvacsej = len(citatele) - 1 - i
        else: # daj na spolocneho menovatela
            idxAktualny = len(citatele) - 1 - i
            citatele[idxNajvacsej] += citatele[idxAktualny] * (4**(idxNajvacsej - idxAktualny))
    
    return redukujNaZakdlandyTvar(citatele[idxNajvacsej], 4**idxNajvacsej)
    
def redukujNaZakdlandyTvar(citatel, menovatel):
    najvacsiSpolocnyDelitel = ea(citatel, menovatel)
    return f"{int(citatel / najvacsiSpolocnyDelitel)}/{int(menovatel / najvacsiSpolocnyDelitel)}"

def ea(r, s):
    if s == 0:
        return r
    
    # r = a * s + z, kde z je zvysok, z >= 0

    return ea(s, r % s)

print(najdiNajvacsiMenovatel())