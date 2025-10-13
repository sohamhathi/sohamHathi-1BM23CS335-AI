# Unification algorithm (fixed parser & example)
import re

def is_variable(x):
    """Variable if it is a string and starts with an uppercase letter."""
    return isinstance(x, str) and len(x) > 0 and x[0].isupper()

def unify(x, y, subs=None):
    if subs is None:
        subs = {}
    if x == y:
        return subs
    if is_variable(x):
        return unify_var(x, y, subs)
    if is_variable(y):
        return unify_var(y, x, subs)
    if isinstance(x, tuple) and isinstance(y, tuple):
        if x[0] != y[0] or len(x[1]) != len(y[1]):
            return None
        for a, b in zip(x[1], y[1]):
            subs = unify(apply_subs(a, subs), apply_subs(b, subs), subs)
            if subs is None:
                return None
        return subs
    return None

def unify_var(var, x, subs):
    if var in subs:
        return unify(subs[var], x, subs)
    elif is_variable(x) and x in subs:
        return unify(var, subs[x], subs)
    elif occur_check(var, x, subs):
        return None
    else:
        subs[var] = x
        return subs

def occur_check(var, x, subs):
    if var == x:
        return True
    elif isinstance(x, tuple):
        return any(occur_check(var, arg, subs) for arg in x[1])
    elif isinstance(x, str) and is_variable(x) and x in subs:
        return occur_check(var, subs[x], subs)
    return False

def apply_subs(term, subs):
    if isinstance(term, str) and is_variable(term) and term in subs:
        return apply_subs(subs[term], subs)
    elif isinstance(term, tuple):
        return (term[0], [apply_subs(t, subs) for t in term[1]])
    return term

def parse_term(expr):
    expr = expr.strip()
    # strip outer braces if present, e.g. "{ ... }"
    if expr.startswith('{') and expr.endswith('}'):
        expr = expr[1:-1].strip()
    if '(' not in expr:
        return expr
    functor = expr[:expr.index('(')].strip()
    args = expr[expr.index('(')+1:-1]
    return (functor, parse_args(args))

def parse_args(s):
    args, level, current = [], 0, ''
    for ch in s:
        if ch == ',' and level == 0:
            args.append(parse_term(current.strip()))
            current = ''
        else:
            if ch == '(':
                level += 1
            elif ch == ')':
                level -= 1
            current += ch
    if current.strip():
        args.append(parse_term(current.strip()))
    return args

# -----------------------------
# Example use (conventional):
# -----------------------------
expr1 = "prime(11)"
expr2 = "prime(Y)"     # NOTE: Y is uppercase -> variable

term1 = parse_term(expr1)
term2 = parse_term(expr2)

result = unify(term1, term2)

if result:
    print("MGU:", result)
else:
    print("❌ No unifier found.")
