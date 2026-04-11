def sat(s: str) -> bool:
    if len(s) != 20:
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    s = "0123210"
    while not sat(s):
        s = s[:-1] + str(int(s[-1]) + 1)
    return s

def sat(s: str) -> bool:
    if len(s) != 20:
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

# Testing
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
