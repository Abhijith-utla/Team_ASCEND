def sat(quine):
    return eval(quine) == quine

def sol():
    return ""

# Checking
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
