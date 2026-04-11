def sat(n: int):
    s = str(n)
    return len(set(s)) == 10

def sol():
    return 1234567890

if __name__ == "__main__":
    assert sat(sol())
