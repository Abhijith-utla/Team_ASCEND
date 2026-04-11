def sat(quine):
    return eval(quine) == quine

def sol():
    return {}

# The following line will assert that `sol` returns an empty dictionary.
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
