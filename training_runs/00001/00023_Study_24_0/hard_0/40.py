def sat(li: List[int]):
    return li.count(17) == 3 and li.count(3) >= 2

def sol():
    return [17, 3, 17]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
