def sat(ls: List[str]):
    return "".join(ls) == str(7 ** 64.5) and all(len(s) == 8 for s in ls)

def sol():
    return [str(7 ** 64.5)[:8]]

print(sol())

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
