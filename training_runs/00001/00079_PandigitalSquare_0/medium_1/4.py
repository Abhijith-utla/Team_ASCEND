def sat(n: int):
    s = str(n * n)
    return set(s) == set("0123456789")

def sol():
    return 100

if __name__ == "__main__":
    assert sat(sol())
