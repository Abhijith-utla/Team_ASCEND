def sat(s: str) -> bool:
    if len(s) != 10 or not s.isalpha():
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    return ''.join([s[i] if i % 2 == 0 else '' for i in range(len(s))])

print(sol())

print(sat(sol()))

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
