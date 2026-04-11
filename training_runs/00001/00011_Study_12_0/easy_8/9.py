def sat(li: List[int]):
    li.insert(0, 2)
    return all(i + j == 3 for i, j in zip(li, [4] + li)) and len(li) == 1001

def sol():
    li = [1]*1000 + [2]
    li.insert(0, 2)
    return all(i + j == 3 for i, j in zip(li, [4] + li)) and len(li) == 1001

if __name__ == "__main__":
    assert sat(sol())
