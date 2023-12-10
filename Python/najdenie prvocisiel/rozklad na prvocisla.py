import os
import math 


ABSPATH_script = os.path.abspath(__file__)
RELPATH_writingFile = os.path.join("..", "vysledok.txt")
ABSPATH_writingFile = os.path.join(ABSPATH_script, RELPATH_writingFile)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True
    

def find_prime_numbers(myNumber: int):
    foundPrimeNumbers = []
    
    for num in range(2, int(math.sqrt(myNumber)+1), ): 
        if is_prime(num):
            while myNumber % num == 0:
                foundPrimeNumbers.append(num)
                myNumber //= num 
    
    #print(myNumber)
    if myNumber > 1:  
        foundPrimeNumbers.append(myNumber)

    return foundPrimeNumbers

user_input = int(input("Zadaj prirodzene cislo ktoreho prvocisla mam najst: "))

primeNumbers = find_prime_numbers(user_input)
writing = f"Ked rozlozime cislo {user_input} na prvocisla dostaneme: {', '.join(list(map(str, primeNumbers)))}"

with open(ABSPATH_writingFile, "w", encoding="utf-8") as file:
    file.write(writing)
print(writing)