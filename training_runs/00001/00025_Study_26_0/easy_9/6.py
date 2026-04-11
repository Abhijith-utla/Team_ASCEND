def sat(ls: List[str]):
    return "".join(ls) == '123456789' and all(len(s) == 9 for s in ls)

def sol():
    return [chr(ord('a') + i) for i in range(9)]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
