def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)])

def sol(li: List[int]):
    for i in range(10):
        if li.count(i) != i:
            return False
    return True

if __name__ == "__main__":
    assert sat(sol())
