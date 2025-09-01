print("soham Hathi")
print("1BM23CS335")

from copy import deepcopy

GOAL_STATE = [[1, 2, 3],
              [8, 0, 4],
              [7, 6, 5]]

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def serialize(state):
    return str(state)

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    neighbors = []
    x, y = find_zero(state)

    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny):
            new_state = deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

def dfs(start_state, max_depth=30):
    visited = set()
    path = []
    solution_path = []
    found = False

    def dfs_recursive(state, depth):
        nonlocal found, solution_path
        if depth > max_depth or found:
            return
        serial = serialize(state)
        if serial in visited:
            return
        visited.add(serial)
        path.append(state)

        if state == GOAL_STATE:
            solution_path = path.copy()
            found = True
            return

        for neighbor in get_neighbors(state):
            dfs_recursive(neighbor, depth + 1)

        path.pop()
        visited.remove(serial)

    dfs_recursive(start_state, 0)

    if found:
        return solution_path, len(solution_path) - 1
    else:
        return None, -1

if __name__ == "__main__":
    start = [[2, 8, 3],
             [1, 6, 4],
             [7, 0, 5]]

    path, cost = dfs(start, max_depth=50)

    if path:
        print(f"DFS found a path with cost = {cost}:")
        for step in path:
            for row in step:
                print(row)
            print("------")
    else:
        print("No solution found within depth limit.")
