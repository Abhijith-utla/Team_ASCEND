def sat(s: str):
    return float(s) + len(s) == 4.5

def sol():
    return "4.5"

# Assertion for the correctness of the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
