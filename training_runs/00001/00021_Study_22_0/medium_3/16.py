def sat(s: str) -> bool:
    if len(s) < 5 or len(s) > 30:
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    return 'sat'

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
