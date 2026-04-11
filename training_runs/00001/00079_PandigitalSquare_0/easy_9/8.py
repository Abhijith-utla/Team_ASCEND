def sat(n: int) -> bool:
    s = str(n)
    return len(s) == len(set(s)) and s.isdigit()

def sol():
    return 0

if __name__ == "__main__":
    assert sat(sol())
