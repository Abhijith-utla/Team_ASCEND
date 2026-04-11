def sat(s: str) -> bool:
    if len(s) != 20:
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    return ''.join(chr(i + ord('A')) for i in range(5)) + ''.join(chr(i + ord('a')) for i in range(5))

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
