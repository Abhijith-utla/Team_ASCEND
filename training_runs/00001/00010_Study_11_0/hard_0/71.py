def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol(ls: List[str]) -> str:
    return str(min(ls))

def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

# Test the function
assert sat(sol(["apple", "banana", "cherry"]))

if __name__ == "__main__":
    assert sat(sol())
