def sat(s: str):
    return str(int(8 ** 2888)).count(s) == 8 and len(s) == 5

def sol():
    return "12321"

# Test case
def test_sol():
    assert sat(sol())

# Run the test
test_sol()

if __name__ == "__main__":
    assert sat(sol())
