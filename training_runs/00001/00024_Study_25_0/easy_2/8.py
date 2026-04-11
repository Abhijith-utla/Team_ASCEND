def sat(s: str, t: str) -> bool:
    return sorted(s) == sorted(t) and s == t[::-1]

def sol():
    return sat('abc', 'cba')

# Run the assertion
assert sat('abc', 'cba')

if __name__ == "__main__":
    assert sat(sol())
