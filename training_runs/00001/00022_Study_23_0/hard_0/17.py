def sat(ls: List[str]):
    return tuple(ls) in zip('dee', 'doo', 'dah!')

def sol() -> str:
    return ','.join(['dee', 'doo', 'dah!'])

assert sat(sol().split(','))

if __name__ == "__main__":
    assert sat(sol())
