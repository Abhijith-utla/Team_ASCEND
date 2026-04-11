def sat(s: str):
    return len(s) == 1000 and sum(c == 'o' for c in s) == 1000

def sol():
    s = 'x' * 1000
    return s

if __name__ == "__main__":
    assert sat(sol())
