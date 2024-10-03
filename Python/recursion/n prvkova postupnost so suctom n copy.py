# N-prvkova mnozina so suctom S 
# neklesajuce -> >=, bez duplikatov 


def find_sequences(n: int, s:int, current_attempt:list=[], start:int=0) -> list:
    if len(current_attempt) == n:
        if sum(current_attempt) == s: #riesenie najdene
            return [current_attempt[:]] # vrat uspesne najdenu kombincaiu vo forme listu na pridanie do zoznamu uspesnych rieseni
        else: 
            return [] # nespravny sucet

    success_list: list = []

    for i in range(start, s+1): # zacat skusat validne hodnoty od posledne pridanej hodnoty
        current_attempt.append(i) # pridaj skusobnu hodnotu
        success_list.extend(find_sequences(n, s, current_attempt, i)) # zavolaj znova pre nasledujuce indexy
        current_attempt.pop() # danu hodnotu zmaz a pokracuj na dalsiu v zozname az do vycerpania


    return success_list 


def makeMirrorImage(num): 
    return (reversed_num:=str(num)[::-1], f"pocet cifier: {len(reversed_num)}") 

#print(makeMirrorImage(1234567890)) 

test_result = find_sequences(3, 8) 

print(f"list of items: {test_result}") 
print(f"dlzka zoznamu: {len(test_result)}") 