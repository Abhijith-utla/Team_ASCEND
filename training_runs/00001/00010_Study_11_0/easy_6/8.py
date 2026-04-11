def sat(ls: List[str]):
    if len(ls) == 0:
        return False
    else:
        return all(len(i) < len(ls[0]) for i in ls)

def sol():
    return True

# Testing the function
assert sat(["dog", "cat", "bat"])
assert not sat(["dog", "cat", "bat", "ant"])

if __name__ == "__main__":
    assert sat(sol())
