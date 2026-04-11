def sat(li: List[int]):
    return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol() -> List[int]:
    li = [i for i in range(999)] + [1000]
    return li

if __name__ == "__main__":
    assert sat(sol())
