def sat(s: str):
    return str(8 ** 2888).count(s) > 8 and len(s) == 3

def sol():
    return str(8 ** 2888).count('888') > 8 and len('888') == 3

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
