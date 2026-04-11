def sat(li: List[int]):
    return li.count(17) == 2 and li.count(3) == 1

def sol():
    li = [1, 2, 3, 17, 2, 3, 17]
    return li.count(17) == 2 and li.count(3) == 1

if __name__ == "__main__":
    assert sat(sol())
