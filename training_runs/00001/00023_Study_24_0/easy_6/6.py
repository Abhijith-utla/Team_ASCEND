def sat(li: List[int]):
    return li.count(17) == 3 and li.count(3) == 1

def sol():
    return [17, 17, 3]

if __name__ == "__main__":
    assert sat(sol())
