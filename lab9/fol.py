print("Soham Hathi")
print("1BM23CS335")
from typing import List, Set

def substitute(clause, var, value):
    """Substitute a variable with a value in a clause."""
    return {literal.replace(var, value) for literal in clause}

def unify(literal1: str, literal2: str):
    """Check if two literals can be unified and return substitution if possible."""
    if literal1.startswith("~"):
        l1_pred = literal1[1:]
        neg1 = True
    else:
        l1_pred = literal1
        neg1 = False

    if literal2.startswith("~"):
        l2_pred = literal2[1:]
        neg2 = True
    else:
        l2_pred = literal2
        neg2 = False

    # Must have same predicate name
    if l1_pred.split("(")[0] != l2_pred.split("(")[0]:
        return None

    # Must be opposite signs for resolution
    if neg1 == neg2:
        return None

    args1 = l1_pred[l1_pred.find("(")+1:-1].split(",")
    args2 = l2_pred[l2_pred.find("(")+1:-1].split(",")

    if len(args1) != len(args2):
        return None

    substitution = {}
    for a1, a2 in zip(args1, args2):
        a1, a2 = a1.strip(), a2.strip()
        # Variable (lowercase) can unify with constant (uppercase)
        if a1[0].islower() and not a2[0].islower():
            substitution[a1] = a2
        elif a2[0].islower() and not a1[0].islower():
            substitution[a2] = a1
        elif a1 != a2:
            return None
    return substitution

def resolve(clause1: Set[str], clause2: Set[str]):
    """Resolve two clauses."""
    resolvents = []
    for lit1 in clause1:
        for lit2 in clause2:
            substitution = unify(lit1, lit2)
            if substitution:
                (var, val) = list(substitution.items())[0]
                new_clause1 = substitute(clause1 - {lit1}, var, val)
                new_clause2 = substitute(clause2 - {lit2}, var, val)
                new_clause = new_clause1.union(new_clause2)
                resolvents.append((lit1, lit2, substitution, new_clause))
    return resolvents

def resolution(kb: List[Set[str]], query: Set[str]) -> bool:
    """Resolution algorithm with step-by-step printing."""
    clauses = kb + [set(f"~{q}" for q in query)]  # Negate query
    step = 1
    print("\n--- Resolution Steps ---")

    while True:
        n = len(clauses)
        pairs = [(clauses[i], clauses[j]) for i in range(n) for j in range(i + 1, n)]
        new = set()

        for (ci, cj) in pairs:
            resolvents = resolve(ci, cj)
            for (lit1, lit2, substitution, result_clause) in resolvents:
                print(f"\nStep {step}:")
                print(f"Resolving {ci} and {cj}")
                print(f" - Unifying {lit1} with {lit2}")
                print(f" - Substitution: {substitution}")
                print(f" - Resulting clause: {result_clause if result_clause else '{}'}")
                step += 1

                if not result_clause:  # Empty clause => proved
                    print("\n❗ Contradiction found — query is proven true.")
                    return True

                new.add(frozenset(result_clause))

        if new.issubset(set(map(frozenset, clauses))):
            print("\nNo new clauses — query cannot be proven.")
            return False

        for c in new:
            if c not in clauses:
                clauses.append(set(c))

def main():
    print("=== First Order Logic Resolution Prover ===")
    n = int(input("Enter number of clauses in the knowledge base: "))

    kb = []
    print("\nEnter each clause separated by OR (|). Use '~' for NOT.\n")

    for i in range(n):
        clause_str = input(f"Clause {i+1}: ").replace(" ", "")
        literals = set(clause_str.split("|"))
        kb.append(literals)

    query_str = input("\nEnter query: ").replace(" ", "")
    query = {query_str}

    print("\n=== Resolution Process ===")
    result = resolution(kb, query)

    print("\n✅ Final Result:", "Proved ✅" if result else "Not Proved ❌")


if __name__ == "__main__":
    main()
