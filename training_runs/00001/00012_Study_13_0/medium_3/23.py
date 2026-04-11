def sat(x: float):
    return str(x - 3.1417).startswith("123.456")

def sol():
    return 3.1417

def sat(x: float):
    return str(x - 3.1417).startswith("123.456")

# test cases
print(sat(sol()))  # False
print(sat(sol() - 1))  # False
print(sat(sol() + 1))  # True

if __name__ == "__main__":
    assert sat(sol())
