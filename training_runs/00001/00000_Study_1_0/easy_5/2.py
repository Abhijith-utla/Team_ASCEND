def sat(s: str):
    return s.count('oo') >= 2

def sol():
    return 'oo' * 10

if __name__ == "__main__":
    assert sat(sol())
