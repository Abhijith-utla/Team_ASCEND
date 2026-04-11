def sat(li: List[int]):
    return set(li) == {34}

def sol():
    return 34

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
