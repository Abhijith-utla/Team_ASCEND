def sat(ls: List[str]):
    return tuple(ls) in zip('dee', 'doo', 'dah!')

def sol():
    return tuple(zip('dee', 'doo', 'dah!'))

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
