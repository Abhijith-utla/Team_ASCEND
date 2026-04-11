def sat(ls: List[str]):
    return "".join(ls) == str(7 ** 64.5)

def sol():
    return [7 ** i for i in range(64)]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
