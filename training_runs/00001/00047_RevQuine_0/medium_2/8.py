def sat(rev_quine: str):
    return eval(rev_quine[::-1]) == rev_quine[::-1]

def sol():
    return ""

# Test
def test_sol():
    assert sat(sol())

# Run test
test_sol()

if __name__ == "__main__":
    assert sat(sol())
