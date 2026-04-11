def sat(li: List[int]) -> bool:
    return sorted(li) == list(range(1, len(li) + 1)) and all(li[i] == i for i in range(len(li)))

def sol():
    return sorted([1, 2, 3, 5, 6]) == list(range(1, 7)) and all([1, 2, 3, 5, 6])

# Test Case
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
