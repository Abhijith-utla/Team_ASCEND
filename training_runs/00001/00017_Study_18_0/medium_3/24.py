def sat(ls: List[str]) -> bool:
    return len(ls) == len(set(ls))

def sol():
    return [1, 2, 3]

if __name__ == "__main__":
    assert sat(sol())
