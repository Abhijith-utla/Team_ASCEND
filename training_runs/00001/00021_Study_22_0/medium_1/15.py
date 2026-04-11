def sat(s: str) -> bool:
    if len(s) != 10 or not s.isalpha():
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    for s in ['abcdab', 'abdcab', 'abcdae', 'abcdea', 'abedcg']:
        if not sat(s):
            return False
    return True

def sat(s: str) -> bool:
    if len(s) != 10 or not s.isalpha():
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

print(sat('abcdab'))
print(sat('abdcab'))
print(sat('abcdae'))
print(sat('abcdea'))
print(sat('abedcg'))

if __name__ == "__main__":
    assert sat(sol())
