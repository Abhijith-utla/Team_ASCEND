def sat(li: List[int]):
    return sorted(li) == list(range(998)) and all(li[i] != i for i in range(998)) and len(li) == 999

def sol():
    return sorted([i+1 for i in range(997)]) + [0]

# assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
