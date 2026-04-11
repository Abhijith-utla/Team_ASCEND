def sat(ls: List[str]):
    if len(ls) == 0:
        return False
    else:
        return all(len(i) == len(ls[0]) for i in ls)

def sol():
    return []

# This is a test to ensure the function 'sat' works correctly.
# The 'assert' statement is used to raise an AssertionError if the condition is false.
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
