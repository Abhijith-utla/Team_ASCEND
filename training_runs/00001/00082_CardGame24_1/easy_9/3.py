def sat(expr):
    return eval(expr, {}, {"__builtins__" : None})

def sol():
    return None

print(sat(sol()))  # This will always return None

if __name__ == "__main__":
    assert sat(sol())
