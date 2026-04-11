def sat(i: int):
    return len(str(i + 1000)) < len(str(i + 1001))

def sol():
    return len(str(int(1000) + 1000)) < len(str(int(1000) + 1001))

# Testing the solution
def test_sol():
    assert sat(1)
    assert not sat(10)
    assert sat(100)
    assert not sat(1000)
    assert sat(10000)
    assert not sat(100000)

# Run the test
test_sol()

if __name__ == "__main__":
    assert sat(sol())
