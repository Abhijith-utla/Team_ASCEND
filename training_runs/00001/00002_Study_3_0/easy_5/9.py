def sat(li: List[int]) -> bool:
    return sorted(li) == list(range(1, len(li) + 1)) and all(li[i] == i for i in range(len(li)))

def sol():
    return sorted([1, 2, 3, 4, 5]) == list(range(1, 6)) and all([i == i for i in range(1, 6)])

if __name__ == "__main__":
    assert sat(sol())
