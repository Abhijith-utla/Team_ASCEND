def sat(ls: List[str]) -> bool:
    return all(s not in ls for s in ls)

def sol():
    return bool(sat(['test1', 'test2', 'test3']))

def sat(ls: List[str]) -> bool:
    return all(s not in ls for s in ls)

# Checker will run: assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
