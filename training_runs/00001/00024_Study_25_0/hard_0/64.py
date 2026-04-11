def sat(s: str):
    return sorted(s) == sorted('Permute me true') and s == s[::-1]

def sol():
    return ''.join(sorted(''.join(sorted(input('Enter a string: ')))))

# Testing the solution
if __name__ == '__main__':
    assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
