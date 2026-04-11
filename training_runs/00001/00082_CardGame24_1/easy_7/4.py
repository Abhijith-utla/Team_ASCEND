def sat(expr):
    return eval(expr)

def sol():
    return None

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
