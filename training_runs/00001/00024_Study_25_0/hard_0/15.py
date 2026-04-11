def sat(s: str):
    return sorted(s) == sorted('Permute me true') and s == s[::-1]

def sol():
    return ''.join(sorted(s for s in 'Permute me true' if s in 'Permute me true'))

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
