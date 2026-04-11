def sat(ls: List[str]):
    return "".join(ls) == '12345678' and all(len(s) == 8 for s in ls)

def sol():
    return [
        '12345678',
        '12345678',
        '12345678',
        '12345678',
        '12345678',
        '12345678',
        '12345678',
        '12345678'
    ]

if __name__ == "__main__":
    assert sat(sol())
