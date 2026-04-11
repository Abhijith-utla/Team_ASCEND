def sat(expr):
    return eval(expr, {}, {"__builtins__" : None})

def sol():
    return 42

if __name__ == "__main__":
    assert sat(sol())
