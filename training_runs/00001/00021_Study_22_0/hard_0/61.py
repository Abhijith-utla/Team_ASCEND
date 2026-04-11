def sat(s: str):
    return s[::2] in s and len(set(s)) == 5

def sol():
    s = 'abcd'
    return s[::2] in s and len(set(s)) == 5

# Testing the function
print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
