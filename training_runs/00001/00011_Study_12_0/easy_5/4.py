def sat(li: List[int]):
    return all(i + j == 4 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    li: List[int] = [int(i) for i in input().split()]
    return sat(li)

def sat(li: List[int]):
    return all(i + j == 4 for i, j in zip([4] + li, li)) and len(li) == 1000

if __name__ == "__main__":
    assert sat(sol())
