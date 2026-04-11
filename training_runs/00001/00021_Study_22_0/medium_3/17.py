def sat(s: str) -> bool:
    if len(s) < 5 or len(s) > 30:
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    s = 'abcba' if random.randint(0, 1) == 0 else 'abcbd'
    return sat(s)

Incorrect pattern:
def sol(x):
    if not isinstance(x, str) or len(x) > 30 or len(x) < 5:
        return False
    return set(x[::2]) == set(x[1::2])

if __name__ == "__main__":
    assert sat(sol())
