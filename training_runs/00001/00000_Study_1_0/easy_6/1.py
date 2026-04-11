def sat(s: str):
    return s.count('oo') <= 1

def sol():
    return sat(s)

if __name__ == "__main__":
    assert sat(sol())
