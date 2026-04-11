def sat(li: List[int]):
    return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    li = [i for i in range(1000) if i % 2 != 0]
    return li

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
