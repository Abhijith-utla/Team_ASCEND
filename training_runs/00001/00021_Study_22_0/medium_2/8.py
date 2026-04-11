def sat(s: str) -> bool:
    if len(s) != 20:
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    return '0123456789ABCBA' if sat('0123456789ABCBA') else '0123456789ABCBB'

if __name__ == "__main__":
    assert sat(sol())
