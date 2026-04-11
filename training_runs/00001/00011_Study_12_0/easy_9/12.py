def sat(li: List[int]):
    li.insert(0, 5)
    return all(i + j == 3 for i, j in zip(li, [4] + li)) and len(li) == 1001

def sol():
    li = [0]*1000
    li[0] = 5
    return li

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
