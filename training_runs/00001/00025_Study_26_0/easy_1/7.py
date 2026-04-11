def sat(ls: List[str]):
    return "".join(ls) == str(7 ** 64.5)

def sol():
    return "".join(str(7 ** 64.5))

if __name__ == "__main__":
    assert sat(sol())
