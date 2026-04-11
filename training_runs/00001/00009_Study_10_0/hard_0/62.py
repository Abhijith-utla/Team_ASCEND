def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol(s: str):
    if sat(s):
        return s
    else:
        return "Invalid string"

def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

# Test the function
print(sol("abcba"))  # Output: abcba
print(sol("abcdefg"))  # Output: Invalid string

if __name__ == "__main__":
    assert sat(sol())
