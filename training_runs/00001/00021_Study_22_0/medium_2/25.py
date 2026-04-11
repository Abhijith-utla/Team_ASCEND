def sat(s: str) -> bool:
    if len(s) != 20:
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    s = input()
    return sat(s)

# Test cases
print(sol("abcdabcdabcd"))  # Expected output: True
print(sol("aabbccddeeff"))  # Expected output: True
print(sol("123456789012"))  # Expected output: False
print(sol("abcdef"))  # Expected output: False
print(sol("aabb"))  # Expected output: False

if __name__ == "__main__":
    assert sat(sol())
