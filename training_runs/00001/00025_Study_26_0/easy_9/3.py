def sat(ls: List[str]):
    return "".join(ls) == '123456789' and all(len(s) == 9 for s in ls)

def sol():
    return [9, 8, 7, 6, 5, 4, 3, 2, 1]

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
