def sat(li: List[int]):
    return all(x == i for i, x in enumerate(li))

def sol():
    return [False] * 10

if __name__ == "__main__":
    assert sat(sol())
