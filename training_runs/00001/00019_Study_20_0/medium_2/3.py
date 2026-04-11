def sat(li: List[int]):
    return all(j in {i} for i, j in enumerate(li))

def sol():
    return {0: 1, 1: 2, 2: 3}

if __name__ == "__main__":
    assert sat(sol())
