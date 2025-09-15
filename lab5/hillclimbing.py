import random
import copy
print("soham Hathi")
print("1BM23CS335") 

N = 4  

def print_board(state):
    for row in range(N):
        line = ""
        for col in range(N):
            if state[col] == row:
                line += " Q "
            else:
                line += " . "
        print(line)
    print()

def heuristic(state):
    """Calculate the number of pairs of queens attacking each other."""
    h = 0
    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                h += 1
    return h

def get_neighbors(state):
    """Generate all neighboring states (each queen moved to another row in its column)."""
    neighbors = []
    for col in range(N):
        for row in range(N):
            if state[col] != row:
                neighbor = list(state)
                neighbor[col] = row
                neighbors.append(neighbor)
    return neighbors

def hill_climbing(initial_state):
    current = initial_state
    step = 0

    while True:
        print(f"\n🔄 Step {step}:")
        print(f"Current state: {current}")
        print(f"Heuristic: {heuristic(current)}")
        print_board(current)

        neighbors = get_neighbors(current)
        neighbor_heuristics = [(neighbor, heuristic(neighbor)) for neighbor in neighbors]

        print("Generated neighbors and their heuristics:")
        for i, (neighbor, h) in enumerate(neighbor_heuristics):
            print(f"{i + 1}. {neighbor} -> h = {h}")

        best_neighbor, best_h = min(neighbor_heuristics, key=lambda x: x[1])

        if best_h >= heuristic(current):
           
            print("\n🚫 Local minimum reached. Stopping.")
            break

        current = best_neighbor
        step += 1

        if best_h == 0:
            print("\n✅ Goal state found!")
            print_board(current)
            break

    return current


random_initial_state = [random.randint(0, N - 1) for _ in range(N)]
print("🎲 Initial Random State:", random_initial_state)

final_state = hill_climbing(random_initial_state)
print("🎯 Final State:", final_state)
print("Final Heuristic:", heuristic(final_state))
