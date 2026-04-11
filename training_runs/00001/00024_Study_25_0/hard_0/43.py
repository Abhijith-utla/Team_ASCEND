def sat(s: str):
    return sorted(s) == sorted('Permute me true') and s == s[::-1]

def sol():
    s = ''.join(sorted(input()))
    return s == s[::-1]

# Test the solution
print(sat(sol()))  # True

if __name__ == "__main__":
    assert sat(sol())
