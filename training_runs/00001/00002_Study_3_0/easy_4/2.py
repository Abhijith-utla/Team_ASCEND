def sat(li: List[int]) -> bool:
    return sorted(li) == list(range(len(li))) and all(li[i] == i for i in range(len(li)))

def sol():
    return [0, 1, 2, 3, 4]

if __name__ == "__main__":
    assert sat(sol())
