def sat(s: str) -> bool:
    if len(s) != 20:
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(20))
    while not sat(s):
        s = ''.join(random.choice(string.ascii_lowercase) for _ in range(20))
    return s

# Test cases
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
