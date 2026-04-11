def sat(expr):
    return eval(expr)

def sol():
    return 42

if __name__ == "__main__":
    assert sat(sol())
