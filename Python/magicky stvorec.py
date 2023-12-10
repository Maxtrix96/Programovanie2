stvorec = [
    [17, 24, 1, 8, 15],
    [23, 5, 7, 14, 16],  
    [4, 6, 13, 20, 22],
    [10, 12, 19, 21, 3],
    [11, 18, 25, 2, 9]
]

stvorcek = [
    [8, 1, 6], #stvorce mam od ChatGPT na testovanie roznych rozhrani
    [3, 5, 7],
    [4, 9, 2]
]

def is_square(parameter): #kontroluje ci su vsetky riadky rovnako dlhe
    for i in range(len(parameter)):
        if len(parameter[i]) != len(parameter):
            return False
    else:
        return True
    
def is_unique(parameter): #kontroluje ci sa v stvorci nenachadzaju duplikaty cisel
    numbers = []
    numbersLoop = []
    for i in range(len(parameter)):
        numbersLoop = [number for number in parameter[i]]
        for j in numbersLoop:
            numbers.append(j)
    numbersSet = set(numbers)
    if len(numbers) == len(numbersSet):
        return True
    else:
        return False

def is_magic_line(paramter): #kontroluje ci sa sumy riadkov rovnaju, vzdi vrati True alebo False a sumu, ktoru ako prvu zisti ze sa nerovna sume prveho riadka a index riadka, kde porovnanie vratilo False (ak sa jeden riadok lisi od prveho = jeden z nich ho kazi)
    lineSum = 0
    lineSums = []
    doubleCheck = []
    for i in range(len(paramter)):
        lineSum = sum(paramter[i])
        lineSums.append(lineSum)
    for i in lineSums:
        doubleCheck.append(lineSums[0] == lineSums[lineSums.index(i)])
        lineSum = lineSums[0]
    if False not in doubleCheck:
        return(True, lineSum)
    else:
        lineSum = lineSums[doubleCheck.index(False)]
        return(False, lineSum, doubleCheck.index(False))

def is_magic_column(parameter): #kontroluje ci sa sumy stlpcov rovnaju, vzdi vrati True alebo False a sumu, ktoru ako prvu zisti ze sa nerovna sume prveho stlpca a index stlpca, kde porovnanie vratilo False (ak sa jeden stlpec lisi od prveho = jeden z nich ho kazi)
    columnSums = []
    columnSum = 0
    column = []
    columns = []
    doubleCheck = []
    for i in range(len(parameter)):
        column = []
        for j in range(len(parameter)):
            column.append(parameter[j][i])
        columns.append(column)
    for i in columns:
        columnSums.append(sum(i))
    for i in columnSums:
        doubleCheck.append(columnSums[0] == columnSums[columnSums.index(i)])
        columnSum = columnSums[0]
    if False not in doubleCheck:
        return(True, columnSum)
    else:
        columnSum = columnSums[doubleCheck.index(False)]
        return(False, columnSum, doubleCheck.index(False))

def is_magic_diagonal(parameter): #vytvori list pre uhlorpiecky a vrati ich sumy
    diagonalSum = 0
    diagonalSums = []
    diagonal = []
    for i in range(len(parameter)):
        diagonal.append(parameter[i][i])
    diagonalSums.append(sum(diagonal))
    reversedLine = []
    reversedSquare = []
    for i in range(len(parameter)):
        reversedLine = parameter[i][::-1]
        reversedSquare.append(reversedLine)
    print(reversedSquare)
    diagonal1 = []
    for i in range(len(reversedSquare)):
        diagonal1.append(reversedSquare[i][i])
    diagonalSums.append(sum(diagonal1))
    
    if diagonalSums[0] == diagonalSums[1]:
        diagonalSum = diagonalSums[0]
        return(True, diagonalSum)
    else:
        return(False, diagonalSum)
    

def is_magic_square(parameter):
    magicLine = is_magic_line(parameter)
    magicColumn = is_magic_column(parameter)
    magicDiagonal = is_magic_diagonal(parameter)
    magicLineSum = magicLine[1]
    magicColumnSum = magicColumn[1]
    magicDiagonalSum = magicDiagonal[1]
    if is_square and is_unique: #skontroluje ci je to stvorec, ktory nema v sebe duplikaty cisel
        if magicLine == magicColumn == magicDiagonal: #skontroluje, ci su vsteky riadky, stlpce a uhlopriecky "magicke" a aku maju sumu
            return(True, magicLineSum, magicColumnSum, magicDiagonalSum) #vrati, ze je stvorec magicky a sumy riadkov, stlpcov a uhlopriecky
        else:
            return(False, magicLine[1], magicLine[2], magicColumn[1], magicColumn[2], magicDiagonal[1]) #vrati, ze stvorec nie je magicky a sumy riadkov, stlpcov a ulhopriecky + v ktorom stlpci a/alebo riadku je duplikat hodnoty
    else:
        return(False, magicLine[1], magicLine[2], magicColumn[1], magicColumn[2], magicDiagonal[1]) #to iste ako to prve False ^



print(is_magic_square(stvorec))