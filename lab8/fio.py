import copy

print("soham Hathi")
print("1BM23CS335")
# --------------------------
# Utility Functions
# --------------------------

def is_variable(x):
    """Return True if x is a variable (starts with lowercase letter)."""
    return isinstance(x, str) and x[0].islower()

def standardize_variables(rule, counter):
    """
    Replace all variables in a rule with new unique ones.
    Returns a new rule with standardized variables.
    """
    mapping = {}
    new_rule = []
    for symbol in rule:
        if is_variable(symbol):
            if symbol not in mapping:
                mapping[symbol] = symbol + str(counter)
                counter += 1
            new_rule.append(mapping[symbol])
        else:
            new_rule.append(symbol)
    return new_rule, counter

def substitute(expr, subs):
    """Substitute variables in an expression with values from subs."""
    if isinstance(expr, list):
        return [substitute(e, subs) for e in expr]
    else:
        return subs.get(expr, expr)

# --------------------------
# Unification
# --------------------------

def unify(x, y, subs=None):
    """Attempt to unify two expressions and return substitution if possible."""
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
            subs = unify(substitute(xi, subs), substitute(yi, subs), subs)
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
    elif occur_check(var, x, subs):
        return False
    else:
        subs[var] = x
        return subs

def occur_check(var, x, subs):
    if var == x:
        return True
    elif isinstance(x, list):
        return any(occur_check(var, xi, subs) for xi in x)
    elif x in subs:
        return occur_check(var, subs[x], subs)
    return False

# --------------------------
# Forward Chaining
# --------------------------

def forward_chain(KB, query):
    """
    KB: dictionary with 'facts' and 'rules'
    Each rule is (premises, conclusion)
    """
    new_facts = set()
    counter = 0

    while True:
        added = False
        for (premises, conclusion) in KB['rules']:
            # standardize variables each time
            standardized_premises, counter = standardize_variables(premises, counter)
            standardized_conclusion, counter = standardize_variables(conclusion, counter)

            # try to find substitutions for all premises
            for fact in KB['facts']:
                subs = unify(standardized_premises, fact)
                if subs:
                    inferred = substitute(standardized_conclusion, subs)
                    inferred_str = str(inferred)
                    if inferred_str not in KB['facts']:
                        KB['facts'].add(inferred_str)
                        new_facts.add(inferred_str)
                        added = True
                        if inferred_str == str(query):
                            return True
        if not added:
            break
    return str(query) in KB['facts']

# --------------------------
# Example: Socrates is Mortal
# --------------------------

KB = {
    'facts': set(["Man(Socrates)"]),
    'rules': [
        (["Man(x)"], ["Mortal(x)"])
    ]
}

query = "Mortal(Socrates)"

result = forward_chain(copy.deepcopy(KB), query)

print("Query:", query)
print("Result:", "✅ TRUE" if result else "❌ FALSE")
print("Final Knowledge Base:", KB['facts'])
