def sat(x: float):
    return str(x - 3.1415).startswith("123.456")

def sol():
    return 3.1415

# Test case
assert sat(sol()) == "123.456"

if __name__ == "__main__":
    assert sat(sol())
