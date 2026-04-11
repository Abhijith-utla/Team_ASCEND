def sat(ls: List[str]) -> bool:
    return all(s not in ls for s in set(ls))

def sol():
    return bool(sat)

def sat(ls: List[str]) -> bool:
    return all(s not in ls for s in set(ls))

if __name__ == "__main__":
    assert sat(sol())
