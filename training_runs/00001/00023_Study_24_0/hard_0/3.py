def sat(li: List[int]):
    return li.count(17) == 3 and li.count(3) >= 2

def sol():
    return [1, 17, 3, 17, 1, 1]

def test():
    assert sat(sol())

test()

if __name__ == "__main__":
    assert sat(sol())
