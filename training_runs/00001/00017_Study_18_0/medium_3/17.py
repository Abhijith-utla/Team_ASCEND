def sat(ls: List[str]) -> bool:
    return len(ls) == len(set(ls))

def sol():
    return [i for i in range(1, 11) if i not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

if __name__ == "__main__":
    assert sat(sol())
