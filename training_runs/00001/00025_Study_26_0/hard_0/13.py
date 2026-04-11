def sat(ls: List[str]):
    return "".join(ls) == str(8 ** 88) and all(len(s) == 8 for s in ls)

def sol():
    return "".join(chr(i + 65) * 8 for i in range(8))

print(sol())

if __name__ == "__main__":
    assert sat(sol())
