def sat(li: List[int]):
    return li.count(17) == 3 and li.count(3) >= 2

def sol():
    return [1, 3, 3, 1, 3]

if __name__ == "__main__":
    assert sat(sol())
