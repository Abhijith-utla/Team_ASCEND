def sat(expr):
    return eval(expr, {}, {})

def sol():
    return 1

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
