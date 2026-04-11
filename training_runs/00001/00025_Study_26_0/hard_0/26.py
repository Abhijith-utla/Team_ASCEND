def sat(ls: List[str]):
    return "".join(ls) == str(8 ** 88) and all(len(s) == 8 for s in ls)

def sol():
    return "".join(["A" * 8] * 8)

assert sat([sol()[i:i+8] for i in range(0, len(sol()), 8)])

if __name__ == "__main__":
    assert sat(sol())
