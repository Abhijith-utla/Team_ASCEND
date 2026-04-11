def sat(li: List[int]):
    return all(j in {i - 1, i + 1, 3 * i} for i, j in zip([0] + li, li + [128]))

def sol():
    return [1, 2, 3, 4, 5]

print(sat(sol()))  # AssertionError: 128 not in {0, 1, 3, 4, 6, 9, 12, 18, 21, 24, 27, 30, 32, 35, 40, 48}

if __name__ == "__main__":
    assert sat(sol())
