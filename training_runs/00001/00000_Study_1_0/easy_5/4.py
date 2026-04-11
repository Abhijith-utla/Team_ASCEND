def sat(s: str):
    return s.count('oo') >= 2

def sol():
    return sat("cooooooooool")

if __name__ == "__main__":
    assert sat(sol())
