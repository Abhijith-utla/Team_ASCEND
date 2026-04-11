def sat(ls: List[str]) -> bool:
    return all(len(set(s)) == len(s) for s in ls)

def sol():
    return sat(["abc", "def", "ghi"])

def sat(ls: List[str]) -> bool:
    return all(len(set(s)) == len(s) for s in ls)

assert sat(["abc", "def", "ghi"])

if __name__ == "__main__":
    assert sat(sol())
