def sat(li: List[int]) -> bool:
    return all(li[i] <= li[i + 1] for i in range(len(li) - 1)) and li[0] <= li[-1]

def sol():
    return [1, 2, 3, 4, 5]

if __name__ == "__main__":
    assert sat(sol())
