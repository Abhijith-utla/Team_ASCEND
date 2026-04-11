def sat(s: str):
    return sorted(s) == sorted('Permute me true') and s == s[::-1]

def sol():
    s = ''.join(sorted(input('Please enter a string: ')))
    return s == s[::-1]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
