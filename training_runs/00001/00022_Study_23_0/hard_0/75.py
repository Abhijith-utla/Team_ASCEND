def sat(ls: List[str]):
    return tuple(ls) in zip('dee', 'doo', 'dah!')

def sol():
    return tuple(map(str, [3, 2, 1]))

print(sol())

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
