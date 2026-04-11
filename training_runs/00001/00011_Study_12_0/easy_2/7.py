def sat(li: List[int]):
    return all(i + j == 2 for i, j in zip([5] + li, li)) and len(li) == 1000

def sol():
    return 1000

# Testing the solution
assert sat([5] + list(range(1, 999)))
assert not sat([5] + list(range(1, 998)))
assert sat([5])
assert not sat([6] + list(range(1, 999)))

if __name__ == "__main__":
    assert sat(sol())
