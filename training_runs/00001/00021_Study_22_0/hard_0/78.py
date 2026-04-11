def sat(s: str):
    return s[::2] in s and len(set(s)) == 5

def sol():
    return 'x' * 1000

# Test
print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
