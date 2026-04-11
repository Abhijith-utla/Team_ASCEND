def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)])

def sol():
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return sat(li)

def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)])

if __name__ == "__main__":
    assert sat(sol())
