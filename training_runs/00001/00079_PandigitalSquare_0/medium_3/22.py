def sat(n: int):
    s = str(n * n)
    return len(s) == len(set(s))

def sol():
    return 123456

if __name__ == "__main__":
    assert sat(sol())
