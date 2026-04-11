def sat(s: str):
    return s[::2] in s and len(set(s)) == 5

def sol():
    s = input("Enter a string: ")
    return sat(s)

def sat(s: str):
    return s[::2] in s and len(set(s)) == 5

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
