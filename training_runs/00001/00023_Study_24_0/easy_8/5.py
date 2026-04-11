def sat(li: List[int]):
    return li.count(17) == 3 and li.count(3) == 1

def sol():
    li = [1, 2, 3, 17, 4, 17, 3, 5]
    return li.count(17) == 3 and li.count(3) == 1

if __name__ == "__main__":
    assert sat(sol())
