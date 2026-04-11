def sat(li: List[int]) -> bool:
    return sorted(li) == list(range(len(li))) and all(li[i] == i for i in range(len(li)))

def sol():
    return sorted([1, 2, 3, 4, 5]) == list(range(1, 6))

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
