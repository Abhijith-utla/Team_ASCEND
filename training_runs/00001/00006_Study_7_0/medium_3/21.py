def sat(s: str):
    return str((8 ** 2888) ** 0.5).count(s) > 8 and len(s) == 3

def sol():
    return str((8 ** 2888) ** 0.5).count("0") > 8 and len("0") == 3

# Checking the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
