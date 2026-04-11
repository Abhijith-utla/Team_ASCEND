def sat(li: List[int]):
    li.insert(0, 4)
    return all(i + j == 3 for i, j in zip(li, [4] + li)) and len(li) == 1001

def sol() -> List[int]:
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    li.insert

if __name__ == "__main__":
    assert sat(sol())
