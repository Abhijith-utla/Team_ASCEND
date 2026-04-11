def sat(s: str) -> bool:
    return len(s) == 10 and s.isalpha() and '0' not in s and '1' not in s

def sol():
    return "912386751"

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
