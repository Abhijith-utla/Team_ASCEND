def sat(ls: List[str]):
    return "".join(ls) == str(7 ** 64.6)

def sol():
    ls = [str(i) for i in range(10)]
    return "".join(ls) == str(7 ** 64.6)

print(sol())

if __name__ == "__main__":
    assert sat(sol())
