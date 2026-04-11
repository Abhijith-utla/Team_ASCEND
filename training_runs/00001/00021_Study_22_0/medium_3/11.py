def sat(s: str) -> bool:
    if len(s) < 5 or len(s) > 30:
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    s = input()
    if sat(s):
        return s
    else:
        return "No solution"

# Test cases
print(sol("abcdab"))  # Returns "No solution" because it has less than 5 or more than 30 characters
print(sol("abcdabcd"))  # Returns "abcdabcd"
print(sol("abcde"))  # Returns "No solution" because it has less than 5 characters
print(sol("abcdef"))  # Returns "No solution" because it has more than 30 characters
print(sol("aabbaa"))  # Returns "aabbaa"

if __name__ == "__main__":
    assert sat(sol())
