def sat(ls: List[str]) -> bool:
    return all(s not in ls for s in set(ls))

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())
