def sat(ls: List[str]):
    return "".join(ls) == str(12345678)

def sol():
    return [str(i) for i in range(1, 8)]

# Test the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
