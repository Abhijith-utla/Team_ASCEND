def sat(ls: List[str]) -> bool:
    return all(s not in ls for s in ls)

def sol():
    ls = ['a', 'b', 'c']
    if sat(ls):
        return "No duplicate items in list"
    else:
        return "Duplicate items in list"

def sat(ls: List[str]) -> bool:
    return all(s not in ls for s in ls)

# Running the assert statement
assert sat(["a", "b", "c"]) == "No duplicate items in list"
assert sat(["a", "b", "c", "a"]) == "Duplicate items in list"

if __name__ == "__main__":
    assert sat(sol())
