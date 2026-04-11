def sat(s: str):
    return s[::2] in s and len(set(s)) == 5

def sol():
    return ''.join(x for i, x in enumerate(s) if i % 2 == 0)

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
