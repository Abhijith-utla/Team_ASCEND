def sat(li: List[int]):
    # Check if all elements in the list are either 2, 3, or 4 times their position
    return all(j in {i - 1, i + 1, 3 * i} for i, j in enumerate(li, start=1))

def sol():
    return [4] * 10 + [3] * 5 + [2] * 5

# The function sat(answer) is already defined by the user and is available for testing.
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
