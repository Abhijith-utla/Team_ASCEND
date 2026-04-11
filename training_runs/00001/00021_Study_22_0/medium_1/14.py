def sat(s: str) -> bool:
    if len(s) != 10 or not s.isalpha():
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    return ''.join(chr(ord('A') + i) + chr(ord('A') + i + 1) for i in range(5))

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
