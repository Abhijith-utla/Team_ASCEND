def sat(quine: str):
    return eval(quine) == quine

def sol():
    return {}

# Testing the solution
assert sat(str(sol()))

if __name__ == "__main__":
    assert sat(sol())
