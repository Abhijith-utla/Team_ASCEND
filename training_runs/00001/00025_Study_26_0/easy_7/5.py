def sat(ls: List[str]):
    return "".join(ls) == '12345678' and all(len(s) == 8 for s in ls)

def sol():
    return [s for s in '12345678']

# Test
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
