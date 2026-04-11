def sat(ls: List[str]):
    return "".join(ls) == '123456789' and all(len(s) == 9 for s in ls)

def sol():
    return [i for i in '123456789']

# Testing
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
