def sat(li: List[int]):
    return all(i + j == 3 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    li = [1] * 999
    li[0] = 4
    return li

if __name__ == "__main__":
    assert sat(sol())
