def sat(ls: List[str]):
    return "".join(ls) == str(8 ** 88) and all(len(s) == 8 for s in ls)

def sol():
    ls = ["12345678", "9abcdef0", "7g9hijk1", "2lmnoqrs", "5rt78uvw", "3defghi"]
    return "".join(ls) == str(8 ** 88) and all(len(s) == 8 for s in ls)

if __name__ == "__main__":
    assert sat(sol())
