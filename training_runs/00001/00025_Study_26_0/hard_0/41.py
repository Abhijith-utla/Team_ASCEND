def sat(ls: List[str]):
    return "".join(ls) == str(8 ** 88) and all(len(s) == 8 for s in ls)

def sol():
    ls = ["Hello", "World"]
    return ls

if __name__ == "__main__":
    assert sat(sol())
