def sat(s: str) -> bool:
    if len(s) != 20:
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    s = '01234'
    return s

if __name__ == "__main__":
    assert sat(sol())
