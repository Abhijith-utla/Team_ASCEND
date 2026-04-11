def sat(s: str):
    return str(8 ** 2888).count(s) > 8 and len(s) == 3

def sol():
    return 8 ** 2888

# This line is necessary for the checker to work correctly.
assert sat(str(sol()))

if __name__ == "__main__":
    assert sat(sol())
