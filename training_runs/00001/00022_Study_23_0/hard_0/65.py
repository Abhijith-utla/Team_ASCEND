def sat(ls: List[str]):
    return tuple(ls) in zip('dee', 'doo', 'dah!')

def sol():
    return tuple(('doo', 'dah!', 'dee'))

if __name__ == "__main__":
    assert sat(sol())
