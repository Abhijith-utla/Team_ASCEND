def sat(x: float):
    return str(x - 3.1417).startswith("123.4567")

def sol():
    return 3.1417

# Testing the function
def test_sol():
    assert sat(sol())

test_sol()

if __name__ == "__main__":
    assert sat(sol())
