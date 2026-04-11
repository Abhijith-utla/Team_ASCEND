def sat(li: List[int]):
    return all(i + j == 5 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    li = [0]*1000
    return sat(li)

if __name__ == "__main__":
    assert sat(sol())
