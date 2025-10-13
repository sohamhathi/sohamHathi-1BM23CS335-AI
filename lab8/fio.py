import copy
from itertools import product

print("Soham Hathi")
print("1BM23CS335")

def is_variable(x):
    return isinstance(x, str) and x[0].islower()

def substitute(expr, subs):
    if isinstance(expr, list):
        return [substitute(e, subs) for e in expr]
    else:
        return subs.get(expr, expr)

def unify(x, y, subs=None):
    if subs is None:
        subs = {}
    if subs is False:
        return False
    elif x == y:
        return subs
    elif is_variable(x):
        return unify_var(x, y, subs)
    elif is_variable(y):
        return unify_var(y, x, subs)
    elif isinstance(x, list) and isinstance(y, list):
        if len(x) != len(y):
            return False
        for xi, yi in zip(x, y):
            subs = unify(xi, yi, subs)
            if subs is False:
                return False
        return subs
    else:
        return False

def unify_var(var, x, subs):
    if var in subs:
        return unify(subs[var], x, subs)
    elif x in subs:
        return unify(var, subs[x], subs)
    else:
        subs[var] = x
        return subs

def forward_chain(KB, query):
    facts = [list(f) for f in KB['facts']]
    added = True

    while added:
        added = False
        for premises, conclusion in KB['rules']:
            all_matches = []
            for premise in premises:
                matches = []
                for fact in facts:
                    subs = unify(premise, fact)
                    if subs:
                        matches.append(subs)
                all_matches.append(matches)
            for combo in product(*all_matches):
                merged = {}
                for subs in combo:
                    merged.update(subs)
                inferred = substitute(conclusion, merged)
                if inferred not in facts:
                    facts.append(inferred)
                    added = True
                    if inferred == query:
                        return True
    return query in facts

# --------------------------
# Knowledge Base
# --------------------------
KB = {
    'facts': [
        ["American", "West"],
        ["Weapon", "Missile"],
        ["Sells", "West", "Missile", "Nono"],
        ["Enemy", "Nono", "America"]
    ],
    'rules': [
        # Rule 1: Enemy of America → Hostile
        ([[ "Enemy", "x", "America" ]], [ "Hostile", "x" ]),
        # Rule 2: American sells weapon to hostile nation → Criminal
        ([[ "American", "x" ], [ "Weapon", "y" ], [ "Sells", "x", "y", "z" ], [ "Hostile", "z" ]],
         [ "Criminal", "x" ])
    ]
}

query = ["Criminal", "West"]
result = forward_chain(copy.deepcopy(KB), query)

print("\nQuery:", query)
print("Result:", "✅ TRUE" if result else "❌ FALSE")
