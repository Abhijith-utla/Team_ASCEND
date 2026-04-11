def sat(s: str):
    return s[::2] in s and len(set(s)) == 5

def sol():
    return '012345'

if __name__ == "__main__":
    assert sat(sol())
