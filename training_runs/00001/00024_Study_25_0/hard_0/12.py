def sat(s: str):
    return sorted(s) == sorted('Permute me true') and s == s[::-1]

def sol():
    return ''.join(sorted(input('Enter a string: '))) == ''.join(sorted('Permute me true')) and ''.join(sorted(input('Enter a string: '))) == ''.join(reversed(sorted('Permute me true')))

# Test case
print(sat(sol()))  # True

if __name__ == "__main__":
    assert sat(sol())
