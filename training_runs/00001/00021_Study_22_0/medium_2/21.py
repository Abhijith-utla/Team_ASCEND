def sat(s: str) -> bool:
    if len(s) != 20:
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    return "".join(chr(int(s[::2]) ^ int(s[1::2])) for s in map(str, range(20)))

# Testing
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
