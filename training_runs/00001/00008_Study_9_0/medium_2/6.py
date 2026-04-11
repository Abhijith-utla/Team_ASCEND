def sat(li: List[int]):
    return [i for i in li if i >= 0] == list(
        "The five boxing wizards jump quickly".split(" "))

def sol():
    return []

# Test the function
def test_sol():
    assert sat(sol())

# Run the test
test_sol()

if __name__ == "__main__":
    assert sat(sol())
