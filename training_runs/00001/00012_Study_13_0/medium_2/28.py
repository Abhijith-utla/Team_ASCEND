def sat(x: float):
    return str(x - 3.1416).startswith("123.456")

def sol():
    return 3.1416

# This will ensure that the solution is correct by comparing the output of the solution with the expected result
assert sat(sol()) == '3.1416'

if __name__ == "__main__":
    assert sat(sol())
