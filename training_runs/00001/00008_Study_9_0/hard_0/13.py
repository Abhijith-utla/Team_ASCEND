def sat(li: List[int]):
    return ["The quick brown fox jumps over the lazy dog"[i] for i in li] == list(
        "The five boxing wizards jump quickly")

def sol():
    return [ord(i) for i in "The quick brown fox jumps over the lazy dog" if i in "aeiouAEIOU"]

# Testing the solution
def test_sol():
    assert sat(sol()) == [105, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]

# Running the test
test_sol()

if __name__ == "__main__":
    assert sat(sol())
