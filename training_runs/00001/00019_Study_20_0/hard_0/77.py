def sat(li: List[int]):
    return all(j in {i - 1, i + 1, 3 * i} for i, j in zip([0] + li, li + [128]))

def sol():
    return {i: {j: sat(i, j) for j in range(i - 1, 3 * i + 2)} for i in range(128)}

def sat(li: List[int]):
    return all(j in {i - 1, i + 1, 3 * i} for i, j in zip([0] + li, li + [128]))

# Checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
