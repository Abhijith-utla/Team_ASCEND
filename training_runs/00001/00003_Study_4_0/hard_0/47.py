def sat(li: List[int]):
    return len(li) == 10 and li.count(li[3]) == 2

def sol() -> int:
    return 42

def sat(li: List[int]) -> bool:
    return len(li) == 10 and li.count(li[3]) == 2

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
