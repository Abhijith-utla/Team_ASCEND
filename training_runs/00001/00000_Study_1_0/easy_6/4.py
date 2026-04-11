def sat(s: str):
    return s.count('oo') <= 1

def sol():
    return 'oo' in 'hello' or 'oo' in 'world'

if __name__ == "__main__":
    assert sat(sol())
