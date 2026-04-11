def sat(expr: str):
    assert len(expr) == 9, "hint: expr is a string of 9 characters"
    expr = expr.replace(" ", "")  # ignore whitespace
    assert expr in "1234567890+-*/()", "Expr can only contain `1234567890+-*/()`"
    return abs(eval(expr) - 24.0) < 1e-6

def sol():
    return "2 4 6 /"

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
