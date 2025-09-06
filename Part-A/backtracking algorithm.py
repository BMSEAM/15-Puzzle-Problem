#backtracking algorithm

N = 4
TARGET = "123456789101112131415-"

def is_solved(board):
    flat = "".join("".join(row) for row in board)
    return flat == TARGET

def board_to_string(board):
    return "".join("".join(row) for row in board)

def find_blank(board):
    for r in range(N):
        for c in range(N):
            if board[r][c] == "-":
                return r, c
    return -1, -1

def puzzle(board, blank_r, blank_c, visited, solution_moves):
    if is_solved(board):
        return True
    
    state = board_to_string(board)
    if state in visited:
        return False
    visited.add(state)

    directions = [(-1, 0, "U"), (1, 0, "D"), (0, -1, "L"), (0, 1, "R")]
    for dr, dc, move in directions:
        nr, nc = blank_r + dr, blank_c + dc
        if 0 <= nr < N and 0 <= nc < N:
            # swap
            board[blank_r][blank_c], board[nr][nc] = board[nr][nc], board[blank_r][blank_c]

            if puzzle(board, nr, nc, visited, solution_moves):
                solution_moves.append(move)
                return True

            # backtrack
            board[blank_r][blank_c], board[nr][nc] = board[nr][nc], board[blank_r][blank_c]
    
    return False
#(b) Print whether the puzzle is solvable and the path taken
def is_solvable_matrix(board):
    N = len(board)
    flat = []
    blank_row = -1
    for r in range(N):
        for c in range(N):
            if board[r][c] == "-":
                blank_row = r
            else:
                flat.append(int(board[r][c]))

    inversions = 0
    for i in range(len(flat)):
        for j in range(i+1, len(flat)):
            if flat[i] > flat[j]:
                inversions += 1

    blank_from_bottom = N - blank_row
    if N % 2 != 0:  
        return inversions % 2 == 0
    else:  
        if blank_from_bottom % 2 == 0:
            return inversions % 2 == 1
        else:
            return inversions % 2 == 0
board = [
    ["1", "2", "3", "4"],
    ["5", "6", "7", "8"],
    ["9", "10", "11", "12"],
    ["13", "15", "14", "-"]
]

visited = set()
solution_moves = []
r, c = find_blank(board)

if is_solvable_matrix(board):
    if puzzle(board, r, c, visited, solution_moves):
        print("Solved!")
        print("Path:", solution_moves[::-1])  # reverse order
    else:
        print("No solution found (search too deep).")
else:
    print("This puzzle configuration is unsolvable.")
