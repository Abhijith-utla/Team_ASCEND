def sat(li: List[int]):
    return li.count(17) == 2 and li.count(3) == 1

def sol():
    li = [1, 2, 17, 3, 3]
    return li.count(17) == 2 and li.count(3) == 1

if __name__ == "__main__":
    assert sat(sol())
