def sat(li: List[int]):
    return all(j in {i - 1, i + 1, 3 * i} for i, j in zip([0] + li, li + [128]))

def sol():
    return [1, 2, 4, 5, 8, 10, 12, 16, 20, 24, 25, 32, 40, 50, 64, 80, 100, 128]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
