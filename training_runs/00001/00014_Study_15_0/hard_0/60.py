def sat(li: List[int]):
    return all(sum(li[:i]) == 2 ** i - 1 for i in range(20))

def sol():
    return 2 ** 20 - 1

# The provided function 'sat' checks if the sum of all elements up to a certain index is equal to 2^index - 1 for all indices from 0 to 19. The expected output is 2^20 - 1.

# Test case
assert sat([1, 2, 3, 4, 5])

if __name__ == "__main__":
    assert sat(sol())
