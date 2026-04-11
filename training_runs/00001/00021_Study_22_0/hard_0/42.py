def sat(s: str):
    return s[::2] in s and len(set(s)) == 5

def sol():
    return "".join([c for i, c in enumerate(s) if i % 2 == 0])

if __name__ == "__main__":
    assert sat(sol())
