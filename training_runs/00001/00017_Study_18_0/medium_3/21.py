def sat(ls: List[str]) -> bool:
    return len(ls) == len(set(ls))

def sol():
    ls = ["cat", "dog", "bat", "ant", "car", "cat"]
    return sat(ls)

def sat(ls: List[str]) -> bool:
    return len(ls) == len(set(ls))

if __name__ == "__main__":
    assert sat(sol())
