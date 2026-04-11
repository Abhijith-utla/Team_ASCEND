def sat(ls: List[str]):
    return tuple(ls) in zip('dee', 'doo', 'dah!')

def sol():
    return tuple(chr(sum(ord(c) for c in 'dee'+'doo'+'dah!')) for _ in range(3))

if __name__ == "__main__":
    assert sat(sol())
