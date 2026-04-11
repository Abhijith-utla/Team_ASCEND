def sat(ls: List[str]):
    return "".join(ls) == str(8 ** 88) and all(len(s) == 8 for s in ls)

def sol():
    return "".join(["8" * 8] * 8)

# Testing the function
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
