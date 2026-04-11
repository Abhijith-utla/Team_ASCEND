def sat(ls: List[str]):
    return tuple(ls) in zip('dee', 'doo', 'dah!')

def sol():
    return tuple(chr(ord('a')+2*i)+chr(ord('b')+2*i) for i in range(3))

if __name__ == "__main__":
    assert sat(sol())
