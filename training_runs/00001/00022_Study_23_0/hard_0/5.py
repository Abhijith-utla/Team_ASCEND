def sat(ls: List[str]):
    return tuple(ls) in zip('dee', 'doo', 'dah!')

def sol():
    return tuple(list('dee') + list('doo') + list('dah!'))

# Do not remove this line, it is used to validate the solution.
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
