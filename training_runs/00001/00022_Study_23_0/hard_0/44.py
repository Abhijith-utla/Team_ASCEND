def sat(ls: List[str]):
    return tuple(ls) in zip('dee', 'doo', 'dah!')

def sol():
    return tuple(ord(c) for c in 'dee' + 'doo' + 'dah!')

# assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
