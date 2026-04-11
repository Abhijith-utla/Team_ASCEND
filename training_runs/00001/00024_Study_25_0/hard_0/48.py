def sat(s: str):
    return sorted(s) == sorted('Permute me true') and s == s[::-1]

def sol():
    return sorted(''.join(sorted(input('Please input a string: ')))) == sorted(''.join(sorted(input('Please input another string: '))))

if __name__ == "__main__":
    assert sat(sol())
