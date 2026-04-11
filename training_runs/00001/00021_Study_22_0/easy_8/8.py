def sat(s: str) -> bool:
    if len(s) > 30 or len(s) < 5:
        return False
    return len(set(s)) == len(s) and s.index(s[0]) == s.index(s[-1])

def sol():
    s = input()
    return sat(s)

if __name__ == "__main__":
    assert sat(sol())
