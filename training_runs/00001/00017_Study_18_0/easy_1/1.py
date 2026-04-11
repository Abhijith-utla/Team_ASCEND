def sat(ls: List[str]) -> bool:
    return len(ls) == len(set(ls))

def sol():
    return sat([1,2,3,4,4,3,2,1])

def sat(ls: List[str]) -> bool:
    return len(ls) == len(set(ls))

if __name__ == "__main__":
    assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
