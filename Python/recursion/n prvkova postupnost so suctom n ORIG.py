# N-prvkova mnozina so suctom S 
# N prvkov, sucet S 
# neklesajuce -> stupajuce, bez duplikatov 


def generate(n: int, s:int) -> list: 
    if s <= 0 or n > s or n <= 0: return [] 

    success_list: list = [] 
    def try_comb(n: int, s:int) -> list: 
        if s <= 0 or n > s or n <= 0: return [] 
        #rek cast
        
        current_attempt: list = [] 
        for i in range(n): 
            options = range(s-n-i, s-i) # vsetky moznosti tohto indexu, s tym, ze neskusa nepotrebne hodnoty 
            for j in range(len(options)): 
                current_attempt.append(options(j)) 
                if sum(current_attempt) == s: 
                    print("found correct sum") 
                    if len(current_attempt) == n: 
                        success_list.append(current_attempt) 
                        print("found ans") 
                        return current_attempt 
                    else: return [] 
                current_attempt + try_comb(n-1, s-i)  
                current_attempt.clear() 
    return success_list 


def makeMirrorImage(num): 
    return (reversed_num:=str(num)[::-1], f"pocet cifier: {len(reversed_num)}") 

 #print(makeMirrorImage(1234567890)) 

test_result = generate(3, 8) 

print(f"list of items: {test_result}") 
print(f"dlzka zoznamu: {len(test_result)}") 