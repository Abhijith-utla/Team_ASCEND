def sat(expr):
    return eval(expr, {}, {"__builtins__" : None})

def sol():
    return 1

# Let's check if it's correct
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
