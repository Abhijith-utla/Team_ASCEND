def sat(expr):
    return eval(expr, {}, {})

def sol():
    return 0

# This checker will run: assert sat(sol())
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
