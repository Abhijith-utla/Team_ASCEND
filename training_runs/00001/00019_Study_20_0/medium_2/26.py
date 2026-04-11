def sat(li: List[int]):
    return all(j in {i} for i, j in enumerate(li))

def sol():
    return {1, 2, 3}

def test():
    assert sat(sol())

test()

if __name__ == "__main__":
    assert sat(sol())
