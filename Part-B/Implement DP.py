#(a) Implement DP with memoization
N = 4
GOAL = tuple(range(1, N * N)) + (0,)

def get_moves(pos):
    x, y = divmod(pos, N)
    moves = []
    if x > 0: moves.append(pos - N)      # up
    if x < N - 1: moves.append(pos + N)  # down
    if y > 0: moves.append(pos - 1)      # left
    if y < N - 1: moves.append(pos + 1)  # right
    return moves

def apply_move(state, blank, new_pos):
    state = list(state)
    state[blank], state[new_pos] = state[new_pos], state[blank]
    return tuple(state), new_pos

def dp_solve(state, blank, memo):
    if state == GOAL:
        return 0  # solved in 0 moves
    
    if state in memo:
        return memo[state]

    min_steps = float("inf")
    for new_pos in get_moves(blank):
        new_state, new_blank = apply_move(state, blank, new_pos)
        steps = dp_solve(new_state, new_blank, memo)
        if steps != -1:  
            min_steps = min(min_steps, 1 + steps)

    memo[state] = -1 if min_steps == float("inf") else min_steps
    return memo[state]
#(c) Print the minimum number of steps to solve
def is_solvable_tuple(state):
    N = int(len(state) ** 0.5)
    flat = [x for x in state if x != 0]
    blank_row = state.index(0) // N
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


# Example puzzle (swapped 14 and 15)
initial = (1, 2, 3, 4,
           5, 6, 7, 8,
           9, 10, 11, 12,
           13, 15, 14, 0)

if is_solvable_tuple(initial):
    blank = initial.index(0)
    memo = {}
    steps = dp_solve(initial, blank, memo)
    if steps == -1:
        print("No solution found (too deep).")
    else:
        print("Minimum steps to solve:", steps)
else:
    print("This puzzle configuration is unsolvable.")
