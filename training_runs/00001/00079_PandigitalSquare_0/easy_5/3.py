def sat(n: int):
    s = str(n * 2)
    return len(set(s)) == 10

def sol():
    return 10

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
