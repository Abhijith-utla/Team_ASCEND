def sat(ls: List[str]) -> bool:
    return all(s not in ls for s in ls)

def sol():
    ls = ['a', 'b', 'c']
    return sat(ls)

sat = lambda ls: all(s not in ls for s in ls)

if __name__ == "__main__":
    assert sat(sol())
