def sat(s: str):
    return str(int(8 ** 2888)).count(s) == 8 and len(s) == 5

def sol():
    return "12321"

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
