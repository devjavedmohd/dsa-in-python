
# def recursive(a, n):
#     if n < a:
#         return
#     if n == a:
#         print(a)
#     else:
#         print(a)
#         recursive(a, n - 1)

# user_input = input("Enter four numbers separated by space or comma: ")

# replace (,) comma to space ( ) and then split them individual items

# split_input = [x.split() for x in user_input.replace(',', ' ').split()]
# split_input = user_input.replace(',', ' ').split()
# print(split_input)

# convert them into integer using int() function python
# numeric_input = [int(x) for x in split_input]
# print(numeric_input)

# Use the unpacking operator * to pass only the first two elements
# if len(numeric_input) >= 2:  # Ensure there are at least two numbers
#     a, n = numeric_input[0], numeric_input[1]  # Assign to variables
#     recursive(a, n)  # Use these variables to call the recursive function
# else:
#     print("Please enter at least two numeric values.")

# *(star) used for multiple values
# recursive(*numeric_input[:2])

# Sudoku solver using backtracking
def solve_sudoku(board):
    # Function to find the next empty cell
    def find_empty(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None

    # Function to check if a number can be placed in a cell
    def is_valid(board, num, pos):
        # Check row
        if num in board[pos[0]]:
            return False
        # Check column
        if num in [board[i][pos[1]] for i in range(9)]:
            return False
        # Check 3x3 box
        box_x = pos[1] // 3
        box_y = pos[0] // 3
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if board[i][j] == num:
                    return False
        return True

    def solve():
        empty = find_empty(board)
        if not empty:
            return True  # All cells are filled, solution found
        row, col = empty

        for num in range(1, 10):
            if is_valid(board, num, (row, col)):
                board[row][col] = num  # Place the number
                if solve():  # Recurse to solve the rest of the board
                    return True
                board[row][col] = 0  # Backtrack if invalid
        return False  # No valid solution

    solve()
    return board


# Example Sudoku board with some empty cells (0 represents empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 0, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

# Solve the Sudoku puzzle
solved_sudoku = solve_sudoku(sudoku_board)

# Print the solved board
for row in solved_sudoku:
    print(row)

def profile_info(username, followers):
    print("Username: " + username)
    print("Followers: " + str(followers))

# Call function with parameters assigned as above
# profile_info("sammyshark", 945)
result = profile_info("sammyshark", 945)
result
print(result)

# Call function with keyword arguments
# profile_info(username="AlexAnglerfish", followers=342)
