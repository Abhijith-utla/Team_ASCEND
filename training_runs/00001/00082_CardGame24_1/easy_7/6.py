def sat(expr):
    return eval(expr)

def sol():
    return 'Hello World'

if __name__ == "__main__":
    assert sat(sol())
