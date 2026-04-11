def sat(s: str) -> bool:
    if len(s) != 10 or not s.isalpha():
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    s = 'abcdxyzef'
    while not sat(s):
        s = ''.join(chr(ord('a') + i) + chr(ord('a') + i + 1) for i in range(10))
    return s

if __name__ == "__main__":
    assert sat(sol())
