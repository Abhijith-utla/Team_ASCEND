def sat(ls: List[str]):
    return "".join(ls) == str(7 ** 64.5) and all(len(s) == 8 for s in ls)

def sol():
    return ["e" * 8, "b" * 8, "c" * 8, "d" * 8]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
