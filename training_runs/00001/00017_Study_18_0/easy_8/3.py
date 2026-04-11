def sat(ls: List[str]) -> bool:
    return len(ls) == len(set(ls))

def sol():
    return bool(sat)

def sat(ls: List[str]) -> bool:
    return len(ls) == len(set(ls))

assert sat(["a", "b", "c"]) == True
assert sat(["a", "b", "c", "a"]) == False
assert sat(["a"]) == True
assert sat([]) == True

if __name__ == "__main__":
    assert sat(sol())
