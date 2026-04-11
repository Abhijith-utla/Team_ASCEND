def sat(li: List[int]):
    return all((j in {i - 1, i + 1, 3 * i} for i, j in zip([0] + li, li + [128])))

def sol():
    li = [2, 3, 4, 5, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19, 20, 22, 23, 24, 25]
    return sat(li)

def sat(li: List[int]):
    return all((j in {i - 1, i + 1, 3 * i} for i, j in zip([0] + li, li + [128])))

if __name__ == "__main__":
    assert sat(sol())
