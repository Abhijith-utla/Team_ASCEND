def sat(s: str) -> bool:
    return s == 'abc4.5' or s == 'abc4.56'

def sol():
    return 'abc4.5' if 4.5 in [float(i) for i in 'abc4.5'] else 'abc4.56'

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
