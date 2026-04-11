def sat(s: str):
    return len(s) == 1000 and sum(c == 'o' for c in s) == 1000

def sol():
    return 'x' * 1000

# Testing the function
print(sat(sol()))  # Should return True

# Checking the function with the test
assert sat(sol())  # Should return True

if __name__ == "__main__":
    assert sat(sol())
