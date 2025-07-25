def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def is_valid(board, row, col, num):
    # Check if the number is not in the current row
    if num in board[row]:
        return False
    
    # Check if the number is not in the current column
    if num in [board[i][col] for i in range(9)]:
        return False
    
    # Check if the number is not in the current 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            # Find an empty cell
            if board[row][col] == 0:
                # Try filling the cell with numbers from 1 to 9
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        # If the number is valid, fill the cell and recursively solve the rest of the board
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        # If the solution is not valid, undo the current cell and try the next number
                        board[row][col] = 0
                # If no number is valid, backtrack to the previous empty cell and try a different number
                return False
    # If all cells are filled, the Sudoku puzzle is solved
    return True

# Example Sudoku board (0 represents empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Sudoku puzzle:")
print_board(sudoku_board)
print("\nSolving...\n")
if solve_sudoku(sudoku_board):
    print("Sudoku solution:")
    print_board(sudoku_board)
else:
    print("No solution exists.")
