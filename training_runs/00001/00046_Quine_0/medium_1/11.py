def sat(quine):
    return eval(quine) == quine

def sol():
    return ""

# This should pass the test.
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
