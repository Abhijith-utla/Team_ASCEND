def sat(li: List[int]):
    return all(j in {i - 1, i + 1, 3 * i} for i, j in zip([0] + li, li + [128]))

def sol():
    return {i: j for i, j in zip([0] + [1 if i == 0 else 3 * i - 1 for i in range(128)], [128] + [i - 1 for i in range(128) if i != 0]) if i == 0}

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
