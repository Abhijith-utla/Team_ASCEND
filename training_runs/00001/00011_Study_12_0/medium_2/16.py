def sat(li: List[int]):
    return all(i + j == 2 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    li = [4] + [0]*998
    return li

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
