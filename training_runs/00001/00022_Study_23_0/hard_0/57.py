def sat(ls: List[str]):
    return tuple(ls) in zip('dee', 'doo', 'dah!')

def sol():
    return [i*2 for i in 'dee']

print(sol())

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
