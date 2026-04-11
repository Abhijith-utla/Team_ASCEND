def sat(ls: List[str]):
    return tuple(ls) in zip('dee', 'doo', 'dah!')

def sol():
    return [a for a, b, c in zip('dee', 'doo', 'dah!')]

# Test
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
