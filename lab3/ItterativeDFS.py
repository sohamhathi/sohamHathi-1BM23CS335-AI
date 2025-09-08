from copy import deepcopy
print("soham Hathi")
print("1BM23CS335")

# Goal state
GOAL_STATE = [[1, 2, 3],
              [8, 0, 4],
              [7, 6, 5]]  

DIRECTIONS = {'UP': (-1, 0), 'DOWN': (1, 0), 'LEFT': (0, -1), 'RIGHT': (0, 1)}

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
    return None


def is_goal(state):
    return state == GOAL_STATE


def get_successors(state):
    successors = []
    x, y = find_blank(state)
    for move, (dx, dy) in DIRECTIONS.items():
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = deepcopy(state)
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            successors.append((new_state, move))
    return successors

def depth_limited_search(state, depth, path, visited):
    if is_goal(state):
        return path

    if depth == 0:
        return None

    visited.append(state)

    for successor, move in get_successors(state):
        if successor not in visited:
            result = depth_limited_search(successor, depth - 1, path + [move], visited)
            if result is not None:
                return result

    visited.pop()
    return None

# Iterative Deepening DFS
def iterative_deepening_search(start_state, max_depth=50):
    for depth in range(max_depth):
        print(f"Trying depth limit: {depth}")
        visited = []
        result = depth_limited_search(start_state, depth, [], visited)
        if result is not None:
            return result
    return None

if __name__ == "__main__":
    
    initial_state = [[2, 8, 3],
                     [1 ,6, 4],
                     [7, 0, 5]]

    solution = iterative_deepening_search(initial_state)

    if solution:
        print("\nSolution found!")
        print("Moves to solve:", solution)
        print("Number of moves:", len(solution))
    else:
        print("No solution found within depth limit.")
