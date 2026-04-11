def sat(li: List[int]):
    return all(j in {i - 1, i + 1, 3 * i} for i, j in zip([0] + li, li + [128]))

def sol():
    li = [i-1 if i % 2 == 0 else i + 1 if i % 3 == 0 else 3 * i for i in range(128)]
    return sat(li)

def sat(li: List[int]):
    return all(j in {i - 1, i + 1, 3 * i} for i, j in zip([0] + li, li + [128]))

if __name__ == "__main__":
    assert sat(sol())
