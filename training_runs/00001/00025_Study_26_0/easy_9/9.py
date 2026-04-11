def sat(ls: List[str]):
    return "".join(ls) == '123456789' and all(len(s) == 9 for s in ls)

def sol():
    ls = ["123456789"]
    return "".join(ls)

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
