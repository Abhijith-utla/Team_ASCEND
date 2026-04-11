def sat(ls: List[str]):
    return "".join(ls) == '12345678' and all(len(s) == 8 for s in ls)

def sol():
    return [chr(ord('a') + i) for i in range(8)]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
