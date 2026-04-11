def sat(n: int) -> bool:
    s = str(n * n)
    return len(s) == len(set(s))

def sol():
    n = 10
    while not sat(n):
        n += 1
    return n

if __name__ == "__main__":
    assert sat(sol())
