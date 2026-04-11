def sat(s: str) -> bool:
    return len(s) == 10 and s.isalpha() and all(s[i] == s[0] for i in range(1, len(s)))

def sol():
    return 'Python'

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
