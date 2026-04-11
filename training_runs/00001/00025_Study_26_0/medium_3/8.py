def sat(ls: List[str]):
    return "".join(ls) == str(987654321) and all(len(s) == 8 for s in ls)

def sol():
    return "98765432"

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
