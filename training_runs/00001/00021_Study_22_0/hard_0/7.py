def sat(s: str):
    return s[::2] in s and len(set(s)) == 5

def sol():
    return ''.join(i for i in range(10) if str(i) in "02468")

print(sol())

if __name__ == "__main__":
    assert sat(sol())
