def sat(ls: List[str]):
    return tuple(ls) in zip('dee', 'doo', 'dah!')

def sol():
    return tuple(ord(ch) for ch in 'dee')

print(sol())

# Checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
