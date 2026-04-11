def sat(expr):
    return eval(expr, {}, {"__builtins__" : None})

def sol():
    return {}

# Testing the function
print(sat(repr(sol())))  # should return {}

if __name__ == "__main__":
    assert sat(sol())
