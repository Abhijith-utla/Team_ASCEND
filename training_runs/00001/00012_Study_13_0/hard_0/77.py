def sat(x: float):
    return str(x - 3.1415).startswith("123.456")

def sol():
    return float(str(3.1415 - 123.456).replace('.', ''))

# Test
assert sat(sol()) == 0.0

if __name__ == "__main__":
    assert sat(sol())
