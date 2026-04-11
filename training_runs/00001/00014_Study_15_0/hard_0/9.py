def sat(li: List[int]):
    return all(sum(li[:i]) == 2 ** i - 1 for i in range(20))

def sol():
    return sum(2 ** i - 1 for i in range(20))

# Test case
assert sat(list(range(1, 21)))

if __name__ == "__main__":
    assert sat(sol())
