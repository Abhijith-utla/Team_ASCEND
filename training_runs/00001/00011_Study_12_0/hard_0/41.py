def sat(li: List[int]):
    return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    li = [i for i in range(1, 1001) if i % 2 == 0]
    return sat(li)

if __name__ == "__main__":
    assert sat(sol())
