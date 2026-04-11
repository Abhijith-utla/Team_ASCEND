def sat(s: str) -> bool:
    if len(s) > 30 or len(s) < 5:
        return False
    return s.count(s[0]) == s.count(s[-1])

def sol():
    s = input()
    while not sat(s):
        s = input()
    return s

print(sol())

if __name__ == "__main__":
    assert sat(sol())
