def sat(li: List[int]):
    return all(i + j == 4 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    return 4

if __name__ == "__main__":
    assert sat(sol())
