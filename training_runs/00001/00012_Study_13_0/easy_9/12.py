def sat(x: float):
    return str(x - 3.1418).startswith("123.456")

def sol():
    return 3.1418

# Testing
assert sat(sol()) == True
assert sat(sol()) == False

if __name__ == "__main__":
    assert sat(sol())
