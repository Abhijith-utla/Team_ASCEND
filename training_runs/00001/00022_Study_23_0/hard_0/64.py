def sat(ls: List[str]):
    return tuple(ls) in zip('dee', 'doo', 'dah!')

def sol():
    return tuple(["d", "e", "e", "o", "o", "a", "h", "!"])

# Check
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
