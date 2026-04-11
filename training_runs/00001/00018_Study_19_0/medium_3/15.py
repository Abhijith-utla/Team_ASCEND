def sat(li: List[int]):
    return set(li) == {0}

def sol():
    return {0}

if __name__ == "__main__":
    assert sat(sol())
