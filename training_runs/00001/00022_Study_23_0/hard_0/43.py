def sat(ls: List[str]):
    return tuple(ls) in zip('dee', 'doo', 'dah!')

def sol() -> List[str]:
    return list(zip('dee', 'doo', 'dah!'))

# Testing the function
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
