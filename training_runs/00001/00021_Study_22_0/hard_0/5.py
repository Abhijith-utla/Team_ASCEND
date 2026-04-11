def sat(s: str):
    return s[::2] in s and len(set(s)) == 5

def sol():
    return "True" if sat("acbbd") else "False"

print(sol())

if __name__ == "__main__":
    assert sat(sol())
