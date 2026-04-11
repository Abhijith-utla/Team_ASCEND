def sat(ls: List[str]):
    return "".join(ls) == str(7 ** 64.5) and all(len(s) == 8 for s in ls)

def sol():
    return [str(i) for i in [7 ** 0.5, 7 ** 1.5, 7 ** 2.5, 7 ** 3.5, 7 ** 4.5, 7 ** 5.5]]

# Test
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
