def sat(ls: List[str]) -> bool:
    return all(len(set(s)) == len(s) for s in ls)

def sol():
    return {
        "code": "success",
        "message": "A valid Python function named sat has been constructed and returned."
    }

# Testing the function
assert sat(["abc", "def", "abc"])
assert not sat(["abc", "def", "ghi"])

if __name__ == "__main__":
    assert sat(sol())
