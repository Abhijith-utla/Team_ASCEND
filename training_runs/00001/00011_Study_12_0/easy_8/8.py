def sat(li: List[int]):
    li.insert(0, 2)
    return all(i + j == 3 for i, j in zip(li, [4] + li)) and len(li) == 1001

def sol():
    li = [1] * 999
    li.insert(0, 2)
    return sat(li)

def sat(li: List[int]):
    li.insert(0, 2)
    return all(i + j == 3 for i, j in zip(li, [4] + li)) and len(li) == 1001

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
