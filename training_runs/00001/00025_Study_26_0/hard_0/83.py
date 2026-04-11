def sat(ls: List[str]):
    return "".join(ls) == str(8 ** 88) and all(len(s) == 8 for s in ls)

def sol():
    return "".join(str(8 ** 88) for _ in range(8))

# Testing
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
