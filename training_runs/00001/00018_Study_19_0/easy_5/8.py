def sat(li: List[int]) -> bool:
    return len(li) == 2 and li[0] == 34 and li[1] == 34

def sol():
    return [34, 34]

if __name__ == "__main__":
    assert sat(sol())
