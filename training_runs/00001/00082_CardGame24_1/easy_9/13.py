def sat(expr):
    return eval(expr, {}, {"__builtins__" : None})

def sol():
    return None

# Testing the function
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
