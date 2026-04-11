def sat(ls: List[str]):
    return "".join(ls) == str(7 ** 64.6)

def sol():
    return [str(int(i ** 64.6)) for i in range(10)]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
