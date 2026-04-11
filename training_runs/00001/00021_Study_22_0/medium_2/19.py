def sat(s: str) -> bool:
    if len(s) != 20:
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    return "aaaaabbbb" if sat("aaaaabbbb") else "bbbbb"

# Testing
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
