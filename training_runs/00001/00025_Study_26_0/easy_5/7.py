def sat(ls: List[str]):
    return "".join(ls) == str(123456789)

def sol():
    return [str(i) for i in range(1, 8)]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
