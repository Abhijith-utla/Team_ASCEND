def sat(s: str) -> bool:
    return sorted(s) == sorted('Auipenmtrs') and s == s[::-1]

def sol():
    return ''.join(sorted(input()))

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
