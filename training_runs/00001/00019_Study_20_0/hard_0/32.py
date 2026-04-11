def sat(li: List[int]):
    return all(j in {i - 1, i + 1, 3 * i} for i, j in zip([0] + li, li + [128]))

def sol():
    li = [i for i in range(128) if i not in {i - 1, i + 1, 3 * i}]
    assert sat(li)
    return li

if __name__ == "__main__":
    assert sat(sol())
