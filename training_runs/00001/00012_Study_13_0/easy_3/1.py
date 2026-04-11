def sat(x: float):
    return x - 3.1415 == 123.456789

def sol():
    return 123.456789

# This is a test to validate the solution
def test_sol():
    result = sol()
    assert sat(result)
test_sol()

if __name__ == "__main__":
    assert sat(sol())
