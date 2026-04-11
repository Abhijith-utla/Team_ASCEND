def sat(li: List[int]):
    return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    return [4] + [i for i in range(1, 1000) if i not in [4] + [j for j in range(1, 1000) if j != i]]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
