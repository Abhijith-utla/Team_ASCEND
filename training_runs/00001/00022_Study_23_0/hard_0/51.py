def sat(ls: List[str]):
    return tuple(ls) in zip('dee', 'doo', 'dah!')

def sol():
    return [['d', 'e', 'e'], ['d', 'o', 'o'], ['d', 'a', 'h', '!']]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
