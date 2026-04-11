def sat(li: List[int]):
    return all(i + j == 2 for i, j in zip([5] + li, li)) and len(li) == 1000

def sol():
    return 1000 - sum(i for i in range(1, 1001) if i not in [5 + j for j in [x for x in range(1, 1001) if i + x == 2]])

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
