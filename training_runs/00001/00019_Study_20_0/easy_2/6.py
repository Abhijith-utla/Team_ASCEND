def sat(li: List[int]):
    # Check if all elements in the list are either 1, 2, or 3 times their position
    return all(j in {i - 1, i + 1, 3 * i} for i, j in enumerate(li, start=1))

def sol():
    return 5

# Check the answer
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
