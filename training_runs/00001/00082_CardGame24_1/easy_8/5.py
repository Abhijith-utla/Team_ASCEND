def sat(expr):
    return eval(expr, {}, {})

def sol():
    return "Test answer"

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
