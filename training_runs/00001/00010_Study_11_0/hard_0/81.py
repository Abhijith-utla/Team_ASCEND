def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    return [len(ls)]

# Test
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
