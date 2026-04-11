def sat(li: List[int]):
    return li.count(1) == 2 and li.count(2) == 2 and li.count(3) == 2 and li.count(4) == 2 and li.count(5) == 2 and li.count(6) == 2 and li.count(7) == 2 and li.count(8) == 2 and li.count(9) == 2

def sol():
    li = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
    return li

if __name__ == "__main__":
    assert sat(sol())
