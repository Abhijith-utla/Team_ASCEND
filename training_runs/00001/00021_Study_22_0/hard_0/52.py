def sat(s: str):
    return s[::2] in s and len(set(s)) == 5

def sol():
    return "true" if sat("abcde") else "false"

if __name__ == "__main__":
    assert sat(sol())
