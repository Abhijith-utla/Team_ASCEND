def sat(s: str) -> bool:
    if len(s) != 20:
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    def sat(s: str) -> bool:
        if len(s) != 20:
            return False
        return len(set(s)) == 5 and s[::2] == s[1::2]

    s = 'abcdefghij'
    while not sat(s):
        s = 'abcdefgh' + s[0]

    return s

if __name__ == "__main__":
    assert sat(sol())
