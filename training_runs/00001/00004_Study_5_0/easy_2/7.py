def sat(li: List[int]):
    return li.count(1) == 5 and li.count(2) == 5 and li.count(3) == 5 and li.count(4) == 5 and li.count(5) == 5 and li.count(6) == 5 and li.count(7) == 5 and li.count(8) == 5 and li.count(9) == 5

def sol() -> int:
    return 7

if __name__ == "__main__":
    assert sat(sol())
