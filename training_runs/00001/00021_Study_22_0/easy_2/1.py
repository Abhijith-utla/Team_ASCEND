def sat(s: str) -> bool:
    return len(s) == 10 and s.isalpha() and '0' not in s and '1' not in s

def sol():
    s = "random0string"  # define the string here
    assert sat(s)
    return s

if __name__ == "__main__":
    assert sat(sol())
