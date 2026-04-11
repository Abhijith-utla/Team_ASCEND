def sat(li: List[int]):
    return li.count(17) == 3 and li.count(3) == 0

def sol():
    return [17, 17, 17] if sat([17, 17, 17, 3, 3]) else [1, 1, 1]

if __name__ == "__main__":
    assert sat(sol())
