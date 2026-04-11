def sat(s: str):
    return str(int(8 ** 2888)).count(s) == 10 and len(s) == 3

def sol():
    return "888"

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
