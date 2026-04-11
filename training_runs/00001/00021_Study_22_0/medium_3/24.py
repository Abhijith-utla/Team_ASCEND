def sat(s: str) -> bool:
    if len(s) < 5 or len(s) > 30:
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    s = 'abcde'
    while not sat(s):
        s = 'abcde' + chr(97 + len(s))
    return s

print(sol())

if __name__ == "__main__":
    assert sat(sol())
