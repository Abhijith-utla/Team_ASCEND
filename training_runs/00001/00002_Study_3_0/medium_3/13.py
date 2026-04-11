def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)-1))

def sol():
    return sorted([i for i in range(1, 1000)])

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
