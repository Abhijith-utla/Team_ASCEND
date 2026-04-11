def sat(li: List[int]):
    return set(li) == {0}

def sol():
    return []

# This is the final checker that will run assert sat(sol())
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
