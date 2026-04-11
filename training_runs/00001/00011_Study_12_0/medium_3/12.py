def sat(li: List[int]):
    return all(i + j == 3 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    li = [4] + [0]*989
    return li

def sat(li: List[int]):
    return all(i + j == 3 for i, j in zip([4] + li, li)) and len(li) == 1000

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
