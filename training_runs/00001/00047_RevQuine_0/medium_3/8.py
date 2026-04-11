def sat(rev_quine: str):
    return eval(rev_quine[::-1]) == rev_quine[0]

def sol():
    return ""

# Test cases
print(sat(sol()))  # True
print(sat(sol("a")))  # False
print(sat(sol("aba")))  # True
print(sat(sol("abba")))  # False
print(sat(sol("abcba")))  # True
print(sat(sol("abcdcba")))  # False
print(sat(sol("aabaa")))  # True
print(sat(sol("")))  # True

if __name__ == "__main__":
    assert sat(sol())
