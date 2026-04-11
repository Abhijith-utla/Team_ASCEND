def sat(ls: List[str]) -> bool:
    return all(len(set(s)) == len(s) for s in ls)

def sol():
    return [len(set(s)) == len(s) for s in ls]

# Assuming that the user has defined 'ls'
assert sat(ls)

if __name__ == "__main__":
    assert sat(sol())
