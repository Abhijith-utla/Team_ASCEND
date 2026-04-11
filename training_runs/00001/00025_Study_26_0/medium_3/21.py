def sat(ls: List[str]):
    return "".join(ls) == str(987654321) and all(len(s) == 8 for s in ls)

def sol():
    return [str(n) for n in [9, 8, 7, 6, 5, 4, 3, 2, 1]]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
