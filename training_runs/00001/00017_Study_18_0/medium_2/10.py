def sat(ls: List[str]) -> bool:
    return all(len(set(s)) == len(s) for s in ls)

def sol():
    def sat(ls: List[str]) -> bool:
        return all(len(set(s)) == len(s) for s in ls)

    assert sat(["abc", "def", "ghi"])
    assert not sat(["abc", "def", "abc"])
    assert sat(["abc", "def", "def"])
    assert not sat(["abc", "def", ""])
    assert not sat(["", "def", "ghi"])
    return True

if __name__ == "__main__":
    assert sat(sol())
