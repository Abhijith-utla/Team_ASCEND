def sat(expr):
    return eval(expr, {}, {})

def sol():
    return {}

if __name__ == "__main__":
    assert sat(sol())
