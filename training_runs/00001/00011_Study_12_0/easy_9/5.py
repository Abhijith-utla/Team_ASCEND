def sat(li: List[int]):
    li.insert(0, 5)
    return all(i + j == 3 for i, j in zip(li, [4] + li)) and len(li) == 1001

def sol():
    return [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5]

if __name__ == "__main__":
    assert sat(sol())
