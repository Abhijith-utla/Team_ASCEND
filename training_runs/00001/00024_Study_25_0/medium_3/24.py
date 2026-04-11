def sat(s: str):
    return sorted(s) == sorted('uipenmtrsA') and s == s[::-1]

def sol():
    return ''.join(sorted(input('Enter a string: ')))

print(sol())

if __name__ == "__main__":
    assert sat(sol())
