def sat(s: str):
    return sorted(s) == sorted('trusenipM') and s == s[::-1]

def sol():
    s = 'trusenipM'
    return s == s[::-1] and sorted(s) == sorted(s)

# Test
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
