def sat(li: List[int]):
    return all(i + j == 3 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    def sat(li: List[int]):
        return all(i + j == 3 for i, j in zip([4] + li, li)) and len(li) == 1000

    li = [1] * 999 + [5]
    assert sat(li)

if __name__ == "__main__":
    assert sat(sol())
