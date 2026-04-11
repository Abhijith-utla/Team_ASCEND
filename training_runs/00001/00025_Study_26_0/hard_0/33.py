def sat(ls: List[str]):
    return "".join(ls) == str(8 ** 88) and all(len(s) == 8 for s in ls)

def sol():
    return "".join(chr(i+96) for i in range(8))

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
