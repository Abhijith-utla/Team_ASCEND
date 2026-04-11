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
print(sol("abcdabcd"))  # "No solution"
print(sol("abcdeabcd"))  # "No solution"
print(sol("abcdeabc"))   # "abcdeabc"
print(sol("abcde"))      # "abcde"

if __name__ == "__main__":
    assert sat(sol())
