def sat(ls: List[str]):
    return "".join(ls) == str(7 ** 64.5) and all(len(s) == 8 for s in ls)

def sol():
    return [chr(int(str(12345678) * 4.5, 16)) * 2 for _ in range(7)]

if __name__ == "__main__":
    assert sat(sol())
