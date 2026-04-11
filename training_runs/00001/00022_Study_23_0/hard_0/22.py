def sat(ls: List[str]):
    return tuple(ls) in zip('dee', 'doo', 'dah!')

def sol():
    return tuple(ls) in zip('dee', 'doo', 'dah!')

def test():
    assert sol() == (('d', 'e', 'e'), ('d', 'o', 'o'), ('d', 'a', 'h', '!'))

if __name__ == "__main__":
    test()

if __name__ == "__main__":
    assert sat(sol())
