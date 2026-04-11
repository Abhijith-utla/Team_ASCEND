def sat(li: List[int]):
    return all([sum(li[:i]) == i for i in range(20)])

def sol():
    def sat(li: List[int]):
        return all([sum(li[:i]) == i for i in range(20)])
    return sat

# Check the function
assert sat([])
assert not sat([1])
assert sat([1, 1])
assert not sat([1, 2])
assert sat([1, 2, 3])
assert not sat([1, 2, 3, 6])
assert sat([1, 2, 3, 6, 10])
assert not sat([1, 2, 3, 6, 10, 15])
assert sat([1, 2, 3, 6, 10, 15, 21])
assert not sat([1, 2, 3, 6, 10, 15, 21, 28])
assert sat([1, 2, 3, 6, 10, 15, 21, 28, 36])
assert not sat([1, 2, 3

if __name__ == "__main__":
    assert sat(sol())
