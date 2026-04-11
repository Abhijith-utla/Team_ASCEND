def sat(li: List[int]):
    return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    return [1] + [3]*987 + [2]

if __name__ == "__main__":
    assert sat(sol())
