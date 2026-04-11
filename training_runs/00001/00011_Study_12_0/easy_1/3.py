def sat(li: List[int]):
    return all(i + j == 1 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol() -> int:
    li = [0]*1000
    return sum(li)

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
