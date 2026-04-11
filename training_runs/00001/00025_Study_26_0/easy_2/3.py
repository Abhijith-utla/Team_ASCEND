def sat(ls: List[str]):
    return all(len(s) == 8 for s in ls)

def sol():
    return ["abcd1234", "abcd1234", "abcd1234", "abcd1234"]

if __name__ == "__main__":
    assert sat(sol())
