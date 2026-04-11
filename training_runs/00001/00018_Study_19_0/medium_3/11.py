def sat(li: List[int]):
    return set(li) == {0}

def sol():
    return 0

# The function sat checks if the list is a set with a single element 0. If it is, it returns True, else False.
def sat(li: List[int]):
    return set(li) == {0}

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
