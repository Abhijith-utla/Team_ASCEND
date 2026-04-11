def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)]) and li.count(0) == 1

def sol():
    li = [1, 2, 2, 3, 0, 0, 0, 1, 1, 1]
    return all([li.count(i) == i for i in range(10)]) and li.count(0) == 1

if __name__ == "__main__":
    assert sat(sol())
