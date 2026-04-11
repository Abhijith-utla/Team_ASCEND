def sat(ls: List[str]):
    return "".join(ls) == str(987654321) and all(len(s) == 8 for s in ls)

def sol():
    return [str(x) for x in range(10000000, 100000000)]

# Test the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
