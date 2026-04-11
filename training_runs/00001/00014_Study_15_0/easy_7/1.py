def sat(li: List[int]):
    return all(x == i for i, x in enumerate(li))

def sol(li: List[int]):
    for i, x in enumerate(li):
        if x != i:
            return False
    return True

if __name__ == "__main__":
    assert sat(sol())
