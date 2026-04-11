def sat(li: List[int]) -> bool:
    return sorted(li) == list(range(999)) and all(li[i] == i for i in range(len(li)))

def sol():
    return sorted([i for i in range(999)]) == list(range(999)) and all([i == i for i in range(999)])

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
