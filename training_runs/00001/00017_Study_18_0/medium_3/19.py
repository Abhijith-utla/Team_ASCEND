def sat(ls: List[str]) -> bool:
    return len(ls) == len(set(ls))

def sol(ls: List[str]) -> bool:
    return len(ls) == len(set(ls))

if __name__ == "__main__":
    assert sat(sol())
