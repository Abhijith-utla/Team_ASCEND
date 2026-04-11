def sat(s: str) -> bool:
    return s == 'abc4.5' or s == 'abc4.56'

def sol():
    return 'abc4.5' if sat('abc4.5') else 'abc4.56'

if __name__ == "__main__":
    assert sat(sol())
