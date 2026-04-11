def sat(li: List[int]) -> bool:
    return len(li) == 1 and li[0] == 34

def sol():
    return [34]

if __name__ == "__main__":
    assert sat(sol())
