def sat(ls: List[str]):
    return "".join(ls) == str(8 ** 88) and all(len(s) == 8 for s in ls)

def sol():
    return "".join(["9" * 8] * 8)

print(sol())

if __name__ == "__main__":
    assert sat(sol())
