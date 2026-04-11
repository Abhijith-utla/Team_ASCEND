def sat(ls: List[str]):
    if len(ls) == 0:
        return True
    else:
        return all(len(set(i)) == len(ls[0]) for i in ls)

def sol():
    return True

# Asserts
assert sat([""]) == True
assert sat(["a", "a"]) == True
assert sat(["a", "b"]) == False
assert sat(["a", "aa"]) == False
assert sat(["aaa", "bbb"]) == False

if __name__ == "__main__":
    assert sat(sol())
