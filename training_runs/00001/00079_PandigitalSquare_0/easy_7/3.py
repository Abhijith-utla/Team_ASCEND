def sat(n: int) -> bool:
    s = str(n)
    return len(s) == len(set(s))

def sol():
    return 123

if __name__ == "__main__":
    assert sat(sol())
