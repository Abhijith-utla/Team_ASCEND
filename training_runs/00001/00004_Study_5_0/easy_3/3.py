def sat(li: List[int]):
    return li.count(1) == 1 and li.count(2) == 1 and li.count(3) == 1 and li.count(4) == 1 and li.count(5) == 1 and li.count(6) == 1 and li.count(7) == 1 and li.count(8) == 1 and li.count(9) == 1

def sol(li: List[int]):
    return 1 in li and 2 in li and 3 in li and 4 in li and 5 in li and 6 in li and 7 in li and 8 in li and 9 in li

print(sol([1, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

if __name__ == "__main__":
    assert sat(sol())
