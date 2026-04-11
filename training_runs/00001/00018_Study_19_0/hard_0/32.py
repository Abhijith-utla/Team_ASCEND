def sat(li: List[int]):
    return {i + j for i in li for j in li} == {0, 1, 2, 3, 4, 5, 6, 17, 18, 19, 20, 34}

def sol():
    return set([i + j for i in range(11) for j in range(11)]) == {0, 1, 2, 3, 4, 5, 6, 17, 18, 19, 20, 34}

if __name__ == "__main__":
    assert sat(sol())
