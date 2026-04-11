def sat(x: float):
    return str(x - 3.1417).startswith("123.456")

def sol():
    return 3.1417

# Checker will call this function and will assert that the result of the function matches the expected result
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
