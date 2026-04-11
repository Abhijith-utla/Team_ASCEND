def sat(li: List[int]):
    return li.count(17) == 3 and li.count(3) >= 2

def sol():
    li = [17, 17, 17, 3, 3, 3]
    assert sat(li)
    return li

if __name__ == "__main__":
    assert sat(sol())
