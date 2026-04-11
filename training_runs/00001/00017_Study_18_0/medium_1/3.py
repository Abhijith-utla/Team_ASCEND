def sat(ls: List[str]) -> bool:
    return all(s not in ls for s in ls)

def sol():
    return not sat(['a', 'b', 'c'])

def sat(ls: List[str]) -> bool:
    return all(s not in ls for s in ls)

assert sat(['a', 'b', 'c']) == False
assert sol() == False

if __name__ == "__main__":
    assert sat(sol())
