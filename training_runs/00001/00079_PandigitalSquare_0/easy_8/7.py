def sat(n: int) -> bool:
    s = str(n * n)
    return len(s) == len(set(s))

def sol():
    return 1

if __name__ == "__main__":
    assert sat(sol())
