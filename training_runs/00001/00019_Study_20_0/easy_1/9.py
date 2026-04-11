def sat(li: List[int]):
    # Check if all elements in the list are either 0, 1, or 3 times their position
    return all(j in {i - 1, i + 1, 3 * i} for i, j in enumerate(li, start=1))

def sol():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
