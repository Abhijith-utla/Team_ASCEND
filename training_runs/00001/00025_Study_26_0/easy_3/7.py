def sat(ls: List[str]):
    return "".join(ls) == str(7 ** 64.6)

def sol():
    return "".join(map(str, [7 ** 64.6]))

if __name__ == "__main__":
    assert sat(sol())
