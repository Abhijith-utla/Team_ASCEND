def sat(li: List[int]):
    return all(j in {i - 1, i + 1, 3 * i} for i, j in zip([0] + li, li + [128]))

def sol():
    li = [3, 2, 1, 5, 6]
    return sat(li)

if __name__ == "__main__":
    assert sat(sol())
