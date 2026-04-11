def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    return "8181818181818181"

# Testing the function
def test_sol():
    assert sat(sol())

# Run the tests
test_sol()

if __name__ == "__main__":
    assert sat(sol())
