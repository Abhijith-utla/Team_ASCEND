def sat(s: str):
    return sorted(s) == sorted('Permute me true') and s == s[::-1]

def sol():
    return ''.join(sorted(input()))

# Test
print(sat(sol()))  # 'aeimnortP'

if __name__ == "__main__":
    assert sat(sol())
