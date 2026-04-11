def sat(x: float):
    return str(x - 3.1417).startswith("123.456")

def sol():
    return 3.1417

# Testing the function
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
