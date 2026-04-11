def sat(s: str):
    return s[::2] in s and len(set(s)) == 5

def sol():
    s = 'abcde'
    while not sat(s):
        s = chr(ord('a') + (ord(s[0]) - ord('a') + 1) % 5) + s[1:]
    return s

if __name__ == "__main__":
    assert sat(sol())
