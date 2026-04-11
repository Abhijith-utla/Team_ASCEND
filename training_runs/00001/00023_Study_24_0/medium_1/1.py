def sat(li: List[int]):
    return li.count(17) == 1 and li.count(3) == 2

def sol():
    return [17, 17, 3, 3]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
