def sat(ls: List[str]) -> bool:
    return len(ls) == len(set(ls))

def sol():
    return sat([1,2,2,3,4,5,5,6])

def sat(ls: List[str]) -> bool:
    return len(ls) == len(set(ls))

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
