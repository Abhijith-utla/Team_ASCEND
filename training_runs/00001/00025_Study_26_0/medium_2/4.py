def sat(ls: List[str]):
    return "".join(ls) == str(12345678) and all(len(s) == 8 for s in ls)

def sol():
    return [str(i) for i in range(10)]

# Test the function
assert sat(sol())

# print(sol())

if __name__ == "__main__":
    assert sat(sol())
