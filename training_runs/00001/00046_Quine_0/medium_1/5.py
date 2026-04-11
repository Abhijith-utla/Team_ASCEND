def sat(quine):
    return eval(quine) == quine

def sol():
    return {}

# This checks if the given solution works correctly
assert sat(sol)

if __name__ == "__main__":
    assert sat(sol())
