def sat(n: int):
    s = str(n * n)
    return len(set(s)) == 10

def sol():
    return {}

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
