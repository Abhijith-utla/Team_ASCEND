def sat(li: List[int]):
    return all(i + j == 2 for i, j in zip([5] + li, li)) and len(li) == 1000

def sol():
    return [1, 2, 3, 4, 5] + [6, 7, 8, 9, 10]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
