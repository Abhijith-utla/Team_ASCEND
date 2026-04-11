def sat(li: List[int]):
    li.insert(0, 2)
    return all(i + j == 3 for i, j in zip(li, [4] + li)) and len(li) == 1001

def sol():
    return [2] + [4]*999

if __name__ == "__main__":
    assert sat(sol())
