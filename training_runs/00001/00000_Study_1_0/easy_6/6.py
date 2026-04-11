def sat(s: str):
    return s.count('oo') <= 1

def sol():
    return 'oo' in 'hello'

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
