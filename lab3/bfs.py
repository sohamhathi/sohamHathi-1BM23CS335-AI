print("soham Hathi")
print("1BM23CS335")
from collections import deque

# Goal state for the 8 puzzle
GOAL_STATE = [[1, 2, 3],
              [8, 0, 4],
              [7, 6, 5]]


DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def serialize(state):
    return str(state)

def deserialize(state_str):
    return eval(state_str)

def get_neighbors(state):
    neighbors = []
   
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j
                break

    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny):
           
            new_state = [row[:] for row in state]
            
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

def bfs(start_state):
    visited = set()
    queue = deque()
    parent_map = {}
    cost_map = {}

    start_serial = serialize(start_state)
    goal_serial = serialize(GOAL_STATE)

    queue.append(start_state)
    visited.add(start_serial)
    parent_map[start_serial] = None
    cost_map[start_serial] = 0

    while queue:
        current_state = queue.popleft()
        current_serial = serialize(current_state)

        if current_serial == goal_serial:
            # Goal reached
            path = []
            while current_serial is not None:
                path.append(deserialize(current_serial))
                current_serial = parent_map[current_serial]
            path.reverse()
            return path, cost_map[serialize(GOAL_STATE)]

        for neighbor in get_neighbors(current_state):
            neighbor_serial = serialize(neighbor)
            if neighbor_serial not in visited:
                visited.add(neighbor_serial)
                queue.append(neighbor)
                parent_map[neighbor_serial] = current_serial
                cost_map[neighbor_serial] = cost_map[current_serial] + 1

    return None, -1  


if __name__ == "__main__":
  
    start = [[2, 8, 3],
             [1, 6, 4],
             [7, 0, 5]]

    path, cost = bfs(start)

    if path:
        print(f"Path to solution (cost = {cost}):")
        for step in path:
            for row in step:
                print(row)
            print("------")
    else:
        print("No solution found.")
