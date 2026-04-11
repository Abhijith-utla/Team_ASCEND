def sat(ls: List[str]) -> bool:
    return all(s not in ls for s in ls)

def sol():
    ls = ['dog', 'cat', 'bird', 'fish']
    return sat(ls)

def sat(ls: List[str]) -> bool:
    return all(s not in ls for s in ls)

if __name__ == "__main__":
    assert sat(sol())
