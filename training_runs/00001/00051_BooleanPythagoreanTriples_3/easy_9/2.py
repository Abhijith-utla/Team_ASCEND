def sat(numbers: List[int], n=4):
    assert len(numbers) >= n
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-n))

def sol():
    return []

# Test cases
assert sat([1, 2, 3, 4, 5])
assert not sat([1, 2, 3, 4, 4])
assert not sat([1, 2, 3, 4, 5, 6, 7])

if __name__ == "__main__":
    assert sat(sol())
