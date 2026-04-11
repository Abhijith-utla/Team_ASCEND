def sat(ls: List[str]):
    return ls[1234] in ls[1235] and ls[1234] != ls[1235]

def sol():
    return 'test' in [1, 2, 3] and 'test' != [1, 2, 3]

if __name__ == "__main__":
    assert sat(sol())
