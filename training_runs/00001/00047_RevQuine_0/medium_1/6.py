def sat(rev_quine: str):
    return eval(rev_quine[::-1]) == rev_quine

def sol():
    return ""

# Test Case
def test_sol():
    assert sat(sol())

# Run Tests
test_sol()

if __name__ == "__main__":
    assert sat(sol())
