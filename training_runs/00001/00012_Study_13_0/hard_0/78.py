def sat(x: float):
    return str(x - 3.1415).startswith("123.456")

def sol():
    return "123.456"

# Testing the solution
def test_sol():
    assert sat(sol())

# Run the tests
test_sol()

if __name__ == "__main__":
    assert sat(sol())
