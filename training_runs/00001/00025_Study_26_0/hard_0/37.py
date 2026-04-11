def sat(ls: List[str]):
    return "".join(ls) == str(8 ** 88) and all(len(s) == 8 for s in ls)

def sol():
    return "".join(["1" * 8] * 88) == str(8 ** 88) and all(len(s) == 8 for s in [f"{i:08b}" for i in range(2 ** 17)])

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
