def sat(li: List[int]) -> bool:
    return all(li[i] <= li[i + 1] for i in range(len(li) - 1)) and li[0] <= li[-1]

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())
