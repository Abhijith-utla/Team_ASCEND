def sat(ls: List[str]) -> bool:
    return all(s not in ls for s in ls)

def sol():
    return False

assert not sat(["hello", "world", "python", "programming", "puzzle"])

if __name__ == "__main__":
    assert sat(sol())
