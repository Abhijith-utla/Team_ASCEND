def sat(li: List[int]):
    return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    return [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
