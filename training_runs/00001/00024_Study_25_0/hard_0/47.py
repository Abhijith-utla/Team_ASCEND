def sat(s: str):
    return sorted(s) == sorted('Permute me true') and s == s[::-1]

def sol():
    s = ''.join(sorted(input('Enter a string: ')))
    return s == s[::-1]

def check_answer():
    assert sat(sol())
check_answer()

if __name__ == "__main__":
    assert sat(sol())
