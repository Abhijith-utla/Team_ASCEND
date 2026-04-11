def sat(li: List[int]) -> bool:
    return sorted(li) == list(range(1, len(li) + 1)) and all(li[i] == i for i in range(len(li)))

def sol():
    li = [3, 1, 4, 2]
    return sat(li)

if __name__ == "__main__":
    assert sat(sol())
