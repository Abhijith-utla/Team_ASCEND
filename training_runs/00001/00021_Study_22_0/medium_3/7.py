def sat(s: str) -> bool:
    if len(s) < 5 or len(s) > 30:
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    s = 'abcba' if sat(s) else 'not_valid'
    return s

if __name__ == "__main__":
    assert sat(sol())
