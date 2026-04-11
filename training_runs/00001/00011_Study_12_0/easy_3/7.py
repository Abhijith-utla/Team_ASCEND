def sat(li: List[int]):
    return all(i + j == 3 for i, j in zip([6] + li, li)) and len(li) == 1000

def sol():
    return 0

def sat(li: List[int]):
    return all(i + j == 3 for i, j in zip([6] + li, li)) and len(li) == 1000

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
