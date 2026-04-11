def sat(expr):
    return eval(expr)

def sol():
    return 42

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
