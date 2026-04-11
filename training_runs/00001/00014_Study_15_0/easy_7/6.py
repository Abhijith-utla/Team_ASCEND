def sat(li: List[int]):
    return all(x == i for i, x in enumerate(li))

def sol():
    return [1, 2, 3]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
