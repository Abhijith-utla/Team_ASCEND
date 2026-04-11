def sat(li: List[int]):
    return li.count(17) == 1 and li.count(3) == 2

def sol():
    li = [17, 3, 17, 3, 17, 1, 1]
    return li

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
