def sat(ls: List[str]):
    return tuple(ls) in zip('dee', 'doo', 'dah!')

def sol():
    return tuple(sorted(['d', 'e', 'o', 'h']))

# Testing the solution
assert sat(sol()) == (('d', 'e', 'o', 'h'),)

if __name__ == "__main__":
    assert sat(sol())
