def sat(ls: List[str]):
    return "".join(ls) == str(12345678) and all(len(s) == 8 for s in ls)

def sol():
    return ["1", "2", "3", "4", "5", "6", "7", "8"]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
