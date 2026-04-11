def sat(numbers: List[int], n=4):
    assert len(numbers) >= n
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-n))

def sol():
    return []

# Test cases
assert sat([])
assert not sat([1])
assert not sat([1, 2])
assert not sat([1, 2, 3])
assert not sat([1, 2, 3, 4])
assert sat([1, 2, 3, 4, 5])
assert not sat([1, 2, 3, 4, 5, 6])
assert not sat([1, 2, 3, 4, 5, 6, 7])
assert not sat([1, 2, 3, 4, 5, 6, 7, 8])
assert not sat([1, 2, 3, 4, 5, 6, 7, 8, 9])
assert not sat([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
assert sat([1, 2, 3, 4, 5, 6, 7, 8, 9, 10

if __name__ == "__main__":
    assert sat(sol())
