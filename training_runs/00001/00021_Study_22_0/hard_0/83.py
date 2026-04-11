def sat(s: str):
    return s[::2] in s and len(set(s)) == 5

def sol():
    return ''.join(s[::2] for s in 'abcdef' if sat(s))

print(sol())

if __name__ == "__main__":
    assert sat(sol())
