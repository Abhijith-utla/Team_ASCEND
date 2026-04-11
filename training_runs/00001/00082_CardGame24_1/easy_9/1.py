def sat(expr):
    return eval(expr, {}, {"__builtins__" : None})

def sol():
    return None

# Testing the correct pattern
expr = 'sol()'
assert sat(expr)

# Testing the incorrect pattern
expr = 'sol(1)'
assert not sat(expr)

if __name__ == "__main__":
    assert sat(sol())
