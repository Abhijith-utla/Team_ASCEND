def sat(s: str):
    return sorted(s) == sorted('Permute me true') and s == s[::-1]

def sol():
    return ''.join(sorted(input())) == ''.join(sorted('Permute me true')) and input() == input()[::-1]

# Test
print(sat(sol()))  # This should print True

if __name__ == "__main__":
    assert sat(sol())
