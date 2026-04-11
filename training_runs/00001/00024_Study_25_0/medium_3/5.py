def sat(s: str):
    return sorted(s) == sorted('uipenmtrsA') and s == s[::-1]

def sol():
    s = ''.join(sorted(input("Enter a string: ")))
    return s == s[::-1]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
