def sat(numbers: List[int], n=2):
    assert len(numbers) >= n
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-n))

def sol():
    return []

# Test cases
assert sat(sol())
assert not sat([])
assert not sat([1])
assert not sat([1, 2])
assert not sat([2, 1])
assert sat([1, 2, 3, 4, 5])
assert not sat([5, 4, 3, 2, 1])
assert not sat([1, 2, 3, 2, 1])
assert not sat([1, 2, 3, 4, 4])
assert not sat([1, 2, 3, 4, 5, 6])

if __name__ == "__main__":
    assert sat(sol())
