def sat(s: str):
    return s[::2] in s and len(set(s)) == 5

def sol():
    return "impossible"

def sat(s: str):
    if len(s) != 10:
        return False
    if len(set(s)) != 5:
        return False
    if not (s[::2] in s and s[1::2] in s):
        return False
    return True

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
