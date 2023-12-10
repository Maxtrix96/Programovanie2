sudokuBoard = [
    [5, 3, 0,   0, 7, 0,   0, 0, 0], 
    [6, 0, 0,   1, 9, 5,   0, 0, 0],
    [0, 9, 8,   0, 0, 0,   0, 6, 0],

    [8, 0, 0,   0, 6, 0,   0, 0, 3],
    [4, 0, 0,   8, 0, 3,   0, 0, 1],
    [7, 0, 0,   0, 2, 0,   0, 0, 6],

    [0, 6, 0,   0, 0, 0,   2, 8, 0],
    [0, 0, 0,   4, 1, 9,   0, 0, 5],
    [0, 0, 0,   0, 8, 0,   0, 7, 9]
]

def is_valid(sudoku, row, col, number):
    if number in sudoku[row]: #riadok
        return False
    
    if number in [sudoku[i][col] for i in range(9)]: #stlpec
        return False

    row3Start = row // 3 * 3#3x3 stvorec
    col3Start = col // 3 * 3
    for i in range(row3Start, row3Start + 3): 
        for j in range(col3Start, col3Start + 3):
            if sudoku[i][j] == number:
                return False

    return True


def solve_sudoku(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                for number in range(1, 10):
                    if is_valid(sudoku, row, col, number):
                        sudoku[row][col] = number
                        if solve_sudoku(sudoku):
                            return True
                        sudoku[row][col] = 0
                return False
    return True

result = solve_sudoku(sudokuBoard)

print(result)
for row in sudokuBoard:
    print(row)

