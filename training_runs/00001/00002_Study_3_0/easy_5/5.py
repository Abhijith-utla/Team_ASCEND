def sat(li: List[int]) -> bool:
    return sorted(li) == list(range(1, len(li) + 1)) and all(li[i] == i for i in range(len(li)))

def sol():
    return [2, 1, 3, 7, 4, 6, 5, 9]

if __name__ == "__main__":
    assert sat(sol())
