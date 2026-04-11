def sat(ls: List[str]):
    return tuple(ls) in zip('dee', 'doo', 'dah!')

def sol():
    return (list(zip('dee', 'doo', 'dah!'))[0])

if __name__ == "__main__":
    assert sat(sol())
