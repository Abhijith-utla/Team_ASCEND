def sat(numbers: List[int], n=2):
    assert len(numbers) >= n
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-n))

def sol():
    return []

# Check the correctness of the solution
assert sat(sol())

# Check the correctness with different inputs
assert not sat(sol([1, 2, 3, 4]))
assert not sat(sol([4, 3, 2, 1]))
assert sat(sol([1, 2, 3, 4, 5, 6]))
assert not sat(sol([1, 2, 3, 3, 2, 1]))

if __name__ == "__main__":
    assert sat(sol())
