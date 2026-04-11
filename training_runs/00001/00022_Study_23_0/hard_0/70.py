def sat(ls: List[str]):
    return tuple(ls) in zip('dee', 'doo', 'dah!')

def sol():
    return tuple(chr(ord('d')+i)+chr(ord('e')+i)+chr(ord('h')+i) for i in range(3))

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
