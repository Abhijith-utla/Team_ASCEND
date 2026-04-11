def sat(li: List[int]):
    return li.count(17) == 3 and li.count(3) >= 2

def sol():
    li = [1, 2, 3, 17, 2, 3, 17, 1, 1]
    return li.count(17) == 3 and li.count(3) >= 2

def test_sol():
    assert sat(sol())

test_sol()

if __name__ == "__main__":
    assert sat(sol())
