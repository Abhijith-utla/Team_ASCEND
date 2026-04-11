def sat(ls: List[str]):
    return tuple(ls) in zip('dee', 'doo', 'dah!')

def sol() -> List[str]:
    return list(zip('dee', 'doo', 'dah!'))

def sat(ls: List[str]) -> bool:
    return list(ls) == list(zip('dee', 'doo', 'dah!'))

def test():
    assert sat(sol())

if __name__ == "__main__":
    test()

if __name__ == "__main__":
    assert sat(sol())
