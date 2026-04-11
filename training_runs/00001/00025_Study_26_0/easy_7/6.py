def sat(ls: List[str]):
    return "".join(ls) == '12345678' and all(len(s) == 8 for s in ls)

def sol():
    return [''.join(chr(ord('A') + i) for i in range(8))]

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
