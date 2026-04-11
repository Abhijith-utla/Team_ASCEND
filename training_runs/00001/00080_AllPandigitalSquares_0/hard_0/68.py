def sat(nums: List[int]):
    return [sorted([int(s) for s in str(n * n)]) for n in set(nums)] == [list(range(10))] * 174

def sol():
    return []

# The test case to verify the solution
def test_sol():
    assert sat([1, 2, 3, 4, 5])
    assert not sat([5, 4, 3, 2, 1])
    assert not sat([1, 2, 2, 4, 5])
    assert not sat([1, 2, 3, 3, 5])
    assert sat([1, 1, 1, 1, 1])

test_sol()

if __name__ == "__main__":
    assert sat(sol())
