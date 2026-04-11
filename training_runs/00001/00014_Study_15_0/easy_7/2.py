def sat(li: List[int]):
    return all(x == i for i, x in enumerate(li))

def sol():
    return [i for i, x in enumerate([1, 1, 1, 2, 1]) if x != i]

if __name__ == "__main__":
    assert sat(sol())
