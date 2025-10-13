import numpy as np
print("soham Hathi")
print("1BM23CS335")

def compute_conflicts(queens):
    """Compute number of pairs of queens attacking each other."""
    conflicts = 0
    n = len(queens)
    for i in range(n):
        for j in range(i + 1, n):
            if queens[i] == queens[j] or abs(queens[i] - queens[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def random_neighbor(queens):
    """Generate a neighbor by swapping two random positions."""
    n = len(queens)
    new_queens = queens.copy()
    i, j = np.random.choice(n, 2, replace=False)
    new_queens[i], new_queens[j] = new_queens[j], new_queens[i]
    return new_queens

def simulated_annealing(n, initial_temp=100, cooling_rate=0.95, max_iter=10000):
    queens = np.arange(n)  # Start with a permutation (0 to n-1)
    current_conflicts = compute_conflicts(queens)
    best_queens = queens.copy()
    best_conflicts = current_conflicts
    temp = initial_temp

    for i in range(max_iter):
        if temp <= 1e-3 or best_conflicts == 0:
            break

        candidate = random_neighbor(queens)
        candidate_conflicts = compute_conflicts(candidate)
        delta = candidate_conflicts - current_conflicts

        if delta < 0 or np.random.rand() < np.exp(-delta / temp):
            queens = candidate
            current_conflicts = candidate_conflicts

            if current_conflicts < best_conflicts:
                best_queens = queens.copy()
                best_conflicts = current_conflicts
        
        temp *= cooling_rate

    return best_queens, n - best_conflicts

n = 8
solution, non_attacking_queens = simulated_annealing(n)
print(f"The best position found is: {solution}")
print(f"The number of queens that are not attacking each other is: {non_attacking_queens}")
