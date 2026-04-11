def sat(ls: List[str]):
    return "".join(ls) == str(8 ** 88) and all(len(s) == 8 for s in ls)

def sol():
    return "".join(["A" * 8] * 88) == str(8 ** 88) and all("".join(["A" * 8] * 8) == str(8 ** 88) for _ in range(88))

if __name__ == "__main__":
    assert sat(sol())
