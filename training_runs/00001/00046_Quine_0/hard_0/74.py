def sat(quine: str):
    return eval(quine) == quine

def sol():
    return eval(str(sol))

# Checker
assert sat(str(sol))

if __name__ == "__main__":
    assert sat(sol())
