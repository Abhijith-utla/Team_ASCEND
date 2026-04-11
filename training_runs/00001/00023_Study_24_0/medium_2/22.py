def sat(li: List[int]):
    return li.count(17) == 2 and li.count(3) == 1

def sol():
    return [17, 17] if sat([17, 17, 3, 3, 3]) else [17, 3] if sat([17, 3, 3, 17, 3]) else [3, 17] if sat([3, 17, 3, 17, 3]) else [3, 3]

if __name__ == "__main__":
    assert sat(sol())
