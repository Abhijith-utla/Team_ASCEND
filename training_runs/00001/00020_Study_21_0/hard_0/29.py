def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3

def sol():
    return [1, 2, 3, 5, 5, 7, 8, 9, 9, 10]

# Test case
def test_sol():
    assert sat(sol())

test_sol()

if __name__ == "__main__":
    assert sat(sol())
