def sat(x: float):
    return str(x - 3.1418).startswith("123.456")

def sol():
    return 123.456

def sat(x: float):
    return str(x - 3.1418).startswith("123.456")

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
