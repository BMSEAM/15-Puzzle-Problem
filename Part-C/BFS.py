#1. Reconstruct the Solution Path
def reconstruct_path(parents, state):
    path = []
    while parents[state][0] is not None:
        state, move = parents[state]
        path.append(move)
    return path[::-1] 
#2. BFS (Shortest Path):
from collections import deque

def bfs(initial):
    if initial == GOAL:
        return []

    blank = initial.index(0)
    q = deque([(initial, blank)])
    parents = {initial: (None, None)}  # state -> (parent, move)

    while q:
        state, blank = q.popleft()
        for new_pos in get_moves(blank):
            new_state, new_blank = apply_move(state, blank, new_pos)
            if new_state not in parents:
                # Record parent and move
                move = new_blank - blank
                if move == -N: mv = "U"
                elif move == N: mv = "D"
                elif move == -1: mv = "L"
                elif move == 1: mv = "R"
                parents[new_state] = (state, mv)
                if new_state == GOAL:
                    return reconstruct_path(parents, new_state)
                q.append((new_state, new_blank))
    return None  # no solution
