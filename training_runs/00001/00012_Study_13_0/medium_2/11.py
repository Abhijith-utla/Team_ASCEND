def sat(x: float):
    return str(x - 3.1416).startswith("123.456")

def sol():
    return 3.1416

# Testing
assert sat(sol()) == True

if __name__ == "__main__":
    assert sat(sol())
