def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3

def sol():
    return [3, 1, 2, 4, 5, 6, 7, 8, 9, 0]

# Testing the function
def test_sol():
    assert sat(sol())

# Running the test
test_sol()

if __name__ == "__main__":
    assert sat(sol())
