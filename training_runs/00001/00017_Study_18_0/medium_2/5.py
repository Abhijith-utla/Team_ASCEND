def sat(ls: List[str]) -> bool:
    return all(len(set(s)) == len(s) for s in ls)

def sol():
    return [x for x in range(10) if sat([str(x) for _ in range(x)])]

def sat(ls: List[str]) -> bool:
    return all(len(set(s)) == len(s) for s in ls)

if __name__ == "__main__":
    assert sat(sol())
