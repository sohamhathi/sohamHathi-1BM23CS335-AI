print("Soham Hathi")
print("1BM23CS335")
import math

# --- Alpha-Beta Search ---
def alpha_beta_search(values, max_depth):
    """Alpha-Beta Search using standard pseudocode."""
    tree = {}         # to store computed node values
    pruned = []       # to store pruned branches

    def max_value(depth, node_index, alpha, beta):
        indent = "   " * depth
        if depth == max_depth:
            print(f"{indent}Leaf Node[{node_index}] = {values[node_index]}")
            tree[(depth, node_index)] = values[node_index]
            return values[node_index]

        print(f"{indent}MAX Node[{node_index}] (α={alpha}, β={beta})")
        v = -math.inf
        for i in range(2):
            child_index = node_index * 2 + i
            val = min_value(depth + 1, child_index, alpha, beta)
            v = max(v, val)
            alpha = max(alpha, v)
            print(f"{indent}→ MAX[{node_index}] updated to {v} (α={alpha}, β={beta})")

            if v >= beta:
                print(f"{indent}⛔ Beta cutoff at Node[{child_index}]")
                pruned.append((depth, node_index, "β"))
                break

        tree[(depth, node_index)] = v
        return v

    def min_value(depth, node_index, alpha, beta):
        indent = "   " * depth
        if depth == max_depth:
            print(f"{indent}Leaf Node[{node_index}] = {values[node_index]}")
            tree[(depth, node_index)] = values[node_index]
            return values[node_index]

        print(f"{indent}MIN Node[{node_index}] (α={alpha}, β={beta})")
        v = math.inf
        for i in range(2):
            child_index = node_index * 2 + i
            val = max_value(depth + 1, child_index, alpha, beta)
            v = min(v, val)
            beta = min(beta, v)
            print(f"{indent}→ MIN[{node_index}] updated to {v} (α={alpha}, β={beta})")

            if v <= alpha:
                print(f"{indent}⛔ Alpha cutoff at Node[{child_index}]")
                pruned.append((depth, node_index, "α"))
                break

        tree[(depth, node_index)] = v
        return v

    print("\n=== Alpha–Beta Search Steps ===")
    best_value = max_value(0, 0, -math.inf, math.inf)
    return best_value, tree, pruned


# --- Function to Print Tree in ASCII ---
def print_tree(values, tree, max_depth):
    print("\n=== TREE STRUCTURE ===")
    index = 0
    for depth in range(max_depth + 1):
        nodes = 2 ** depth
        line = ""
        for i in range(nodes):
            if (depth, i) in tree:
                val = tree[(depth, i)]
            else:
                val = "—"
            line += f"[{val:^5}] "
        print("   " * (max_depth - depth) + line)
    print()


# --- Main Program ---
def main():
    print("=== Alpha–Beta Search Algorithm (Text Tree Output) ===")
    max_depth = int(input("Enter maximum depth of tree (e.g., 3): "))
    num_leaves = 2 ** max_depth

    print(f"\nEnter {num_leaves} leaf node values (space-separated):")
    values = list(map(int, input().split()))

    if len(values) != num_leaves:
        print(f"Error: Expected {num_leaves} values for a complete binary tree.")
        return

    best_value, tree, pruned = alpha_beta_search(values, max_depth)

    print_tree(values, tree, max_depth)

    print("=== RESULTS ===")
    print(f"Optimal root node value: {best_value}")
    if pruned:
        print("Pruned branches:")
        for p in pruned:
            print(f"   Node[{p[1]}] at depth {p[0]} ({p[2]} cutoff)")
    else:
        print("No pruning occurred.")


if __name__ == "__main__":
    main()
